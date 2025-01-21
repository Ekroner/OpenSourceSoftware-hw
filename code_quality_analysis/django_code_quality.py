import libcst as cst
import os
from typing import Dict, List, Set, Tuple
from pathlib import Path
import radon.cli.harvest as harv
from pyflakes.api import checkPath
from pyflakes.reporter import Reporter
from io import StringIO
import sys

class UnusedVariableReporter(Reporter):
    def __init__(self):
        self.warnings = []

    def unexpectedError(self, filename, msg):
        self.warnings.append(f"Unexpected error in {filename}: {msg}")

    def syntaxError(self, filename, msg, lineno, offset, text):
        self.warnings.append(f"Syntax error in {filename}: {msg}")

    def flake(self, message):
        if "unused variable" in str(message).lower() or "imported but unused" in str(message).lower():
            self.warnings.append(str(message))

class ComplexityVisitor(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self.complexity = 0
        self.current_function = None
        self.function_complexities = {}

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        """分析函数定义"""
        self.current_function = node.name.value
        self.function_complexities[self.current_function] = 0

    def leave_FunctionDef(self, node: cst.FunctionDef) -> None:
        self.current_function = None

    def visit_If(self, node: cst.If) -> None:
        """分析if语句复杂度"""
        self.complexity += 1
        if self.current_function:
            self.function_complexities[self.current_function] += 1

    def visit_While(self, node: cst.While) -> None:
        """分析while循环复杂度"""
        self.complexity += 1
        if self.current_function:
            self.function_complexities[self.current_function] += 1

    def visit_For(self, node: cst.For) -> None:
        """分析for循环复杂度"""
        self.complexity += 1
        if self.current_function:
            self.function_complexities[self.current_function] += 1

class CodeComplexityAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = project_path
        self.analysis_results = {}
        
    def find_duplicate_code(self) -> List[Dict]:
        """检测重复代码"""
        try:

            config = {
                'min': 5, 
                'ignore': [],
                'exclude': [],
                'ignore_below': 5
            }
            duplicates = harv.CCHarvester([self.project_path], config).run()
            return self._process_duplicates(duplicates)
        except Exception as e:
            print(f"检测重复代码时出错: {str(e)}")
            return []

    def _process_duplicates(self, duplicates: List) -> List[Dict]:
        """处理重复代码检测结果"""
        processed_duplicates = []
        for dup in duplicates:
            if isinstance(dup, tuple) and len(dup) >= 2:
                blocks = dup[1]
                if blocks:
                    processed_duplicates.append({
                        'lines': len(blocks[0].source),
                        'locations': [
                            {
                                'file': block.filename,
                                'start_line': block.start_line,
                                'end_line': block.end_line
                            }
                            for block in blocks
                        ]
                    })
        return processed_duplicates

    def check_unused_variables(self, file_path: str) -> List[str]:
        """检测未使用的变量"""
        reporter = UnusedVariableReporter()
        checkPath(file_path, reporter)
        return reporter.warnings

    def analyze_file(self, file_path: str) -> Dict:
        """分析单个文件的复杂度和未使用变量"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                try:
                    tree = cst.parse_module(content)
                    visitor = ComplexityVisitor()
                    tree.visit(visitor)
                    

                    unused_vars = self.check_unused_variables(file_path)
                    
                    return {
                        'complexity': visitor.complexity,
                        'function_complexities': visitor.function_complexities,
                        'line_count': len(content.splitlines()),
                        'unused_variables': unused_vars
                    }
                except cst.ParserSyntaxError as e:
                    print(f"语法解析错误 {file_path}: {str(e)}")
                    return None
        except Exception as e:
            print(f"读取文件错误 {file_path}: {str(e)}")
            return None

    def analyze_project(self) -> None:
        """分析整个项目"""
        print(f"开始分析项目: {self.project_path}")
        

        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    result = self.analyze_file(file_path)
                    if result:
                        self.analysis_results[file_path] = result
        

        duplicate_code = self.find_duplicate_code()
        
        self._print_summary(duplicate_code)

    def _print_summary(self, duplicate_code: List[Dict]) -> None:
        """打印分析摘要"""
        print("\n=== 代码质量分析摘要 ===")
        
        if not self.analysis_results:
            print("没有找到可分析的文件！")
            return
            
        total_files = len(self.analysis_results)
        total_complexity = sum(result['complexity'] for result in self.analysis_results.values())
        avg_complexity = total_complexity / total_files
        
        print(f"\n基本统计:")
        print(f"分析的文件总数: {total_files}")
        print(f"总复杂度: {total_complexity}")
        print(f"平均复杂度: {avg_complexity:.2f}")

        print("\n复杂度最高的文件:")
        sorted_files = sorted(
            self.analysis_results.items(), 
            key=lambda x: x[1]['complexity'], 
            reverse=True
        )
        for file_path, result in sorted_files[:5]:
            print(f"- {file_path}: 复杂度 {result['complexity']}")

        print("\n未使用变量:")
        for file_path, result in self.analysis_results.items():
            if result.get('unused_variables'):
                print(f"\n{file_path}:")
                for warning in result['unused_variables']:
                    print(f"  - {warning}")

        print("\n重复代码块:")
        for dup in duplicate_code:
            print(f"\n重复代码 ({dup['lines']} 行):")
            for loc in dup['locations']:
                print(f"  - {loc['file']}:{loc['start_line']}-{loc['end_line']}")

def main():
    project_path = "django/django"  
    analyzer = CodeComplexityAnalyzer(project_path)
    analyzer.analyze_project()

if __name__ == "__main__":
    main() 