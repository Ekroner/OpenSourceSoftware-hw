### 1. 圈复杂度 

圈复杂度的计算原理：

基本定义：表示代码中线性独立路径的数量

计算方法：从1开始，每出现一个控制流语句就+1

统计的控制语句包括：

if/elif/else

for 循环

while 循环

case 语句（match-case）

and/or 运算符

异常处理（try-except）

### 2. 重复代码检测

实现原理：

代码分块：将代码分成小块（通常是函数级别）

标准化：移除空白、注释等非本质内容

散列比较：计算代码块的散列值

本代码中使用的是 radon 库来进行重复代码检测

### 3. 未使用变量检测

实现原理：

符号表构建：

收集所有变量定义

记录变量的作用域

追踪导入语句

使用分析：

遍历代码中的变量引用

标记已使用的变量

对比定义和使用

警告生成：

未使用的局部变量

未使用的导入

未使用的函数参数

```
=== 代码质量分析摘要 ===

基本统计:
分析的文件总数: 881
总复杂度: 11754
平均复杂度: 13.34

复杂度最高的文件:

- django/django\db\models\sql\query.py: 复杂度 331
- django/django\db\models\base.py: 复杂度 328
- django/django\db\models\query.py: 复杂度 277
- django/django\db\models\sql\compiler.py: 复杂度 266
- django/django\db\models\fields\__init__.py: 复杂度 224

未使用变量:

django/django\contrib\gis\db\models\__init__.py:

  - django/django\contrib\gis\db\models\__init__.py:1:1: 'django.db.models.*' imported but unused
  - django/django\contrib\gis\db\models\__init__.py:4:1: 'django.contrib.gis.db.models.lookups' imported but unused
  - django/django\contrib\gis\db\models\__init__.py:5:1: 'django.contrib.gis.db.models.aggregates.*' imported but unused

django/django\contrib\gis\forms\__init__.py:

  - django/django\contrib\gis\forms\__init__.py:1:1: 'django.forms.*' imported but unused
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.GeometryCollectionField' imported but unused 
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.GeometryField' imported but unused
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.LineStringField' imported but unused
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.MultiLineStringField' imported but unused    
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.MultiPointField' imported but unused
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.MultiPolygonField' imported but unused       
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.PointField' imported but unused
  - django/django\contrib\gis\forms\__init__.py:3:1: '.fields.PolygonField' imported but unused
  - django/django\contrib\gis\forms\__init__.py:13:1: '.widgets.BaseGeometryWidget' imported but unused    
  - django/django\contrib\gis\forms\__init__.py:13:1: '.widgets.OpenLayersWidget' imported but unused      
  - django/django\contrib\gis\forms\__init__.py:13:1: '.widgets.OSMWidget' imported but unused

django/django\contrib\gis\geos\__init__.py:

  - django/django\contrib\gis\geos\__init__.py:6:1: '.collections.GeometryCollection' imported but unused  
  - django/django\contrib\gis\geos\__init__.py:6:1: '.collections.MultiLineString' imported but unused     
  - django/django\contrib\gis\geos\__init__.py:6:1: '.collections.MultiPoint' imported but unused
  - django/django\contrib\gis\geos\__init__.py:6:1: '.collections.MultiPolygon' imported but unused        
  - django/django\contrib\gis\geos\__init__.py:12:1: '.error.GEOSException' imported but unused
  - django/django\contrib\gis\geos\__init__.py:13:1: '.factory.fromfile' imported but unused
  - django/django\contrib\gis\geos\__init__.py:13:1: '.factory.fromstr' imported but unused
  - django/django\contrib\gis\geos\__init__.py:14:1: '.geometry.GEOSGeometry' imported but unused
  - django/django\contrib\gis\geos\__init__.py:14:1: '.geometry.hex_regex' imported but unused
  - django/django\contrib\gis\geos\__init__.py:14:1: '.geometry.wkt_regex' imported but unused
  - django/django\contrib\gis\geos\__init__.py:15:1: '.io.WKBReader' imported but unused
  - django/django\contrib\gis\geos\__init__.py:15:1: '.io.WKBWriter' imported but unused
  - django/django\contrib\gis\geos\__init__.py:15:1: '.io.WKTReader' imported but unused
  - django/django\contrib\gis\geos\__init__.py:15:1: '.io.WKTWriter' imported but unused
  - django/django\contrib\gis\geos\__init__.py:16:1: '.libgeos.geos_version' imported but unused
  - django/django\contrib\gis\geos\__init__.py:17:1: '.linestring.LinearRing' imported but unused
  - django/django\contrib\gis\geos\__init__.py:17:1: '.linestring.LineString' imported but unused
  - django/django\contrib\gis\geos\__init__.py:18:1: '.point.Point' imported but unused
  - django/django\contrib\gis\geos\__init__.py:19:1: '.polygon.Polygon' imported but unused

django/django\contrib\gis\geos\prototypes\__init__.py:

  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.create_cs' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_clone' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_getdims' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_getordinate' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_getsize' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_getx' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_gety' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_getz' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_is_ccw' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_setordinate' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_setx' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_sety' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.cs_setz' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:7:1: 'django.contrib.gis.geos.prototypes.coordseq.get_cs' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.create_collection' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.create_empty_polygon' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.create_linearring' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.create_linestring' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.create_point' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.create_polygon' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.destroy_geom' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.geom_clone' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.geos_get_srid' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.geos_makevalid' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.geos_normalize' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.geos_set_srid' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.geos_type' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.geos_typeid' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.get_dims' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.get_extring' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.get_geomn' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.get_intring' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.get_nrings' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.get_num_coords' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:23:1: 'django.contrib.gis.geos.prototypes.geom.get_num_geoms' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:46:1: 'django.contrib.gis.geos.prototypes.misc.*' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_contains' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_covers' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_crosses' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_disjoint' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_equals' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_equalsexact' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_equalsidentical' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_hasz' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_intersects' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_isclosed' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_isempty' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_isring' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_issimple' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_isvalid' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_overlaps' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_relatepattern' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_touches' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:47:1: 'django.contrib.gis.geos.prototypes.predicates.geos_within' imported but unused
  - django/django\contrib\gis\geos\prototypes\__init__.py:67:1: 'django.contrib.gis.geos.prototypes.topology.*' imported but unused

django/django\contrib\messages\__init__.py:

  - django/django\contrib\messages\__init__.py:1:1: 'django.contrib.messages.api.*' imported but unused    
  - django/django\contrib\messages\__init__.py:2:1: 'django.contrib.messages.constants.*' imported but unused
  - django/django\contrib\messages\__init__.py:3:1: 'django.contrib.messages.storage.base.Message' imported but unused

django/django\contrib\postgres\aggregates\__init__.py:

  - django/django\contrib\postgres\aggregates\__init__.py:1:1: '.general.*' imported but unused
  - django/django\contrib\postgres\aggregates\__init__.py:2:1: '.statistics.*' imported but unused

django/django\contrib\postgres\fields\__init__.py:

  - django/django\contrib\postgres\fields\__init__.py:1:1: '.array.*' imported but unused
  - django/django\contrib\postgres\fields\__init__.py:2:1: '.citext.*' imported but unused
  - django/django\contrib\postgres\fields\__init__.py:3:1: '.hstore.*' imported but unused
  - django/django\contrib\postgres\fields\__init__.py:4:1: '.jsonb.*' imported but unused
  - django/django\contrib\postgres\fields\__init__.py:5:1: '.ranges.*' imported but unused

django/django\contrib\postgres\forms\__init__.py:

  - django/django\contrib\postgres\forms\__init__.py:1:1: '.array.*' imported but unused
  - django/django\contrib\postgres\forms\__init__.py:2:1: '.hstore.*' imported but unused
  - django/django\contrib\postgres\forms\__init__.py:3:1: '.ranges.*' imported but unused

django/django\core\checks\__init__.py:

  - django/django\core\checks\__init__.py:29:1: 'django.core.checks.urls' imported but unused

django/django\db\utils.py:

  - django/django\db\utils.py:8:1: 'django.utils.connection.ConnectionDoesNotExist' imported but unused    

django/django\db\backends\postgresql\psycopg_any.py:

  - django/django\db\backends\postgresql\psycopg_any.py:77:5: 'psycopg2.errors' imported but unused        
  - django/django\db\backends\postgresql\psycopg_any.py:78:5: 'psycopg2.extras.Inet' imported but unused   

django/django\db\migrations\writer.py:

  - django/django\db\migrations\writer.py:9:1: 'django.conf.SettingsReference' imported but unused

django/django\db\migrations\__init__.py:

  - django/django\db\migrations\__init__.py:1:1: '.migration.Migration' imported but unused
  - django/django\db\migrations\__init__.py:1:1: '.migration.swappable_dependency' imported but unused     
  - django/django\db\migrations\__init__.py:2:1: '.operations.*' imported but unused

django/django\db\models\__init__.py:

  - django/django\db\models\__init__.py:3:1: 'django.db.models.aggregates.*' imported but unused
  - django/django\db\models\__init__.py:5:1: 'django.db.models.constraints.*' imported but unused
  - django/django\db\models\__init__.py:18:1: 'django.db.models.enums.*' imported but unused
  - django/django\db\models\__init__.py:39:1: 'django.db.models.fields.*' imported but unused
  - django/django\db\models\__init__.py:46:1: 'django.db.models.indexes.*' imported but unused

django/django\db\models\fields\files.py:

  - django/django\db\models\fields\files.py:440:13: 'PIL.Image' imported but unused

django/django\db\models\sql\__init__.py:

  - django/django\db\models\sql\__init__.py:1:1: 'django.db.models.sql.query.*' imported but unused        
  - django/django\db\models\sql\__init__.py:3:1: 'django.db.models.sql.subqueries.*' imported but unused   

django/django\dispatch\__init__.py:

  - django/django\dispatch\__init__.py:9:1: 'django.dispatch.dispatcher.Signal' imported but unused        
  - django/django\dispatch\__init__.py:9:1: 'django.dispatch.dispatcher.receiver' imported but unused      

django/django\forms\__init__.py:

  - django/django\forms\__init__.py:5:1: 'django.core.exceptions.ValidationError' imported but unused      
  - django/django\forms\__init__.py:6:1: 'django.forms.boundfield.*' imported but unused
  - django/django\forms\__init__.py:7:1: 'django.forms.fields.*' imported but unused
  - django/django\forms\__init__.py:8:1: 'django.forms.forms.*' imported but unused
  - django/django\forms\__init__.py:9:1: 'django.forms.formsets.*' imported but unused
  - django/django\forms\__init__.py:10:1: 'django.forms.models.*' imported but unused
  - django/django\forms\__init__.py:11:1: 'django.forms.widgets.*' imported but unused

django/django\template\__init__.py:

  - django/django\template\__init__.py:55:1: '.base.VariableDoesNotExist' imported but unused
  - django/django\template\__init__.py:56:1: '.context.ContextPopException' imported but unused
  - django/django\template\__init__.py:57:1: '.exceptions.TemplateDoesNotExist' imported but unused        
  - django/django\template\__init__.py:57:1: '.exceptions.TemplateSyntaxError' imported but unused
  - django/django\template\__init__.py:60:1: '.base.Node' imported but unused
  - django/django\template\__init__.py:60:1: '.base.NodeList' imported but unused
  - django/django\template\__init__.py:60:1: '.base.Origin' imported but unused
  - django/django\template\__init__.py:60:1: '.base.Variable' imported but unused
  - django/django\template\__init__.py:69:1: '.library.Library' imported but unused
  - django/django\template\__init__.py:72:1: '.autoreload' imported but unused

django/django\test\selenium.py:

  - Syntax error in django/django\test\selenium.py: invalid syntax

django/django\utils\choices.py:

  - Syntax error in django/django\utils\choices.py: invalid syntax

重复代码块:
```

