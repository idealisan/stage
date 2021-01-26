<div id="home" style="margin-top: 416px;">
<div id="header">
	<div id="blogTitle">
        <a id="lnkBlogLogo" href="https://www.cnblogs.com/linzhenyu/"><img id="blogLogo" src="/skins/custom/images/logo.gif" alt="返回主页"></a>		
		
<!--done-->
<h1><a id="Header1_HeaderTitle" class="headermaintitle HeaderMainTitle" href="https://www.cnblogs.com/linzhenyu/">林震宇</a>
</h1>
<h2>think more) do more) love more) make more money)</h2>




		
	</div><!--end: blogTitle 博客的标题和副标题 -->
	<div id="navigator">
		
<ul id="navList">
<li><a id="blog_nav_sitehome" class="menu" href="https://www.cnblogs.com/">
博客园</a>
</li>
<li>
<a id="blog_nav_myhome" class="menu" href="https://www.cnblogs.com/linzhenyu/">
首页</a>
</li>
<li>

<a id="blog_nav_newpost" class="menu" href="https://i.cnblogs.com/EditPosts.aspx?opt=1">
新随笔</a>
</li>
<li>
<a id="blog_nav_contact" class="menu" href="https://msg.cnblogs.com/send/%E6%9E%97%E9%9C%87%E5%AE%87">
联系</a></li>
<li>
<a id="blog_nav_rss" class="menu" href="javascript:void(0)" data-rss="https://www.cnblogs.com/linzhenyu/rss/">订阅</a>
<!--<partial name="./Shared/_XmlLink.cshtml" model="Model" /></li>--></li>
<li>
<a id="blog_nav_admin" class="menu" href="https://i.cnblogs.com/">
管理</a>
</li>
</ul>


		<div class="blogStats">
			<span id="stats_post_count">随笔 - 55&nbsp; </span>
<span id="stats_article_count">文章 - 1&nbsp; </span>
<span id="stats-comment_count">评论 - 9</span>

		</div><!--end: blogStats -->
	</div><!--end: navigator 博客导航栏 -->
</div><!--end: header 头部 -->
<div id="main">
	<div id="mainContent">
	<div class="forFlow">
		<div id="post_detail">
    <!--done-->
    <div id="topics">
        <div class="post">
            <h1 class="postTitle">
                
<a id="cb_post_title_url" class="postTitle2 vertical-middle post-del-title" href="https://www.cnblogs.com/linzhenyu/p/13206761.html">
    <span>KDD MIMIC-III数据集介绍</span>
    


</a>

            </h1>
            <div class="clear"></div>
            <div class="postBody">
                
    <div id="cnblogs_post_description" style="display: none">
        MIMIC-III 数据库 详细信息介绍 表格内容详情
    </div>
<div id="cnblogs_post_body" class="blogpost-body cnblogs-markdown">
    <span title-type="h1" class="header__span" style="transform:scale(1.0);"><h1 id="mimic-iii" tid="tid-eXkw4m" class="header__dev"><span style=""><b class="dev__fe"><i>1</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>0</i></b></span><b class="dev__developer"><span class="dev__title">MIMIC-III</span></b></h1></span>
<blockquote>
<p>免费公开的重症监护医学信息数据库。包含2001年至2012年之间进入重症监护病房的成年患者的53423例不同的医院入院数据和2001年至2008年之间收治的7870名新生儿数据。</p>
</blockquote>
<p><a href="https://mimic.physionet.org/" target="_blank">Home</a> | <a href="https://github.com/MIT-LCP/mimic-code" target="_blank">Github</a> | <a href="https://mimic.physionet.org/about/mimic/" target="_blank">Doc</a></p>
<span title-type="h1" class="header__span" style="transform:scale(1.0);"><h1 id="字典信息数据" tid="tid-PDrNTy" class="header__dev"><span style=""><b class="dev__fe"><i>2</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>0</i></b></span><b class="dev__developer"><span class="dev__title">字典信息数据</span></b></h1></span>
<blockquote>
<p>字典信息数据，共包含5个数据表。抽取患者的数据比如说生命体征,心率等,实验室指标(如白细胞红细胞等)等, 需要在相应的字典中找到相应的item,即项目标识符,再对应查找某一个患者对应指标下的数据</p>
</blockquote>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="d_cpt" tid="tid-FakpNj" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>2</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>1</i></b></span><b class="dev__developer"><span class="dev__title">d_cpt</span></b></h2></span>
<blockquote>
<p>操作记录代码索引</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>行号</td>
</tr>
<tr>
<td>CATEGORY</td>
<td>SMALLINT</td>
<td>CPT code 类别号</td>
</tr>
<tr>
<td>SECTIONRANGE</td>
<td>VARCHAR(100)</td>
<td>给定的代码范围</td>
</tr>
<tr>
<td>SECTIONHEADER</td>
<td>VARCHAR(50)</td>
<td>给定的代码说明</td>
</tr>
<tr>
<td>SUBSECTIONRANGE</td>
<td>VARCHAR(100)</td>
<td>更多有用的信息</td>
</tr>
<tr>
<td>SUBSECTIONHEADER</td>
<td>VARCHAR(300)</td>
<td>更多有用的信息</td>
</tr>
<tr>
<td>CODESUFFIX</td>
<td>VARCHAR(5)</td>
<td>-</td>
</tr>
<tr>
<td>MINCODEINSUBSECTION</td>
<td>INT</td>
<td>SUBSECTIONRANGE 的最小值</td>
</tr>
<tr>
<td>MAXCODEINSUBSECTION</td>
<td>INT</td>
<td>SUBSECTIONRANGE 的最大值</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="d_icd_diagnoses" tid="tid-CFrBSa" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>2</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>2</i></b></span><b class="dev__developer"><span class="dev__title">d_icd_diagnoses</span></b></h2></span>
<blockquote>
<p>诊断代码索引</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICD9_CODE</td>
<td>VARCHAR(10)</td>
<td>ICD-9 编码</td>
</tr>
<tr>
<td>SHORT_TITLE</td>
<td>VARCHAR(50)</td>
<td>缩写</td>
</tr>
<tr>
<td>LONG_TITLE</td>
<td>VARCHAR(300)</td>
<td>全称</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="d_icd_procedures" tid="tid-2QcRdB" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>2</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>3</i></b></span><b class="dev__developer"><span class="dev__title">d_icd_procedures</span></b></h2></span>
<blockquote>
<p>手术操作代码索引</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICD9_CODE</td>
<td>VARCHAR(10)</td>
<td>ICD-9 编码</td>
</tr>
<tr>
<td>SHORT_TITLE</td>
<td>VARCHAR(50)</td>
<td>缩写</td>
</tr>
<tr>
<td>LONG_TITLE</td>
<td>VARCHAR(300)</td>
<td>全称</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="d_items" tid="tid-RhQmGe" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>2</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>4</i></b></span><b class="dev__developer"><span class="dev__title">d_items</span></b></h2></span>
<blockquote>
<p>记录项目代码索引</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>项目标识符</td>
</tr>
<tr>
<td>LABEL</td>
<td>VARCHAR(200)</td>
<td>项目标签</td>
</tr>
<tr>
<td>ABBREVIATION</td>
<td>VARCHAR(100)</td>
<td>标签缩写</td>
</tr>
<tr>
<td>DBSOURCE</td>
<td>VARCHAR(20)</td>
<td>数据来源</td>
</tr>
<tr>
<td>LINKSTO</td>
<td>VARCHAR(50)</td>
<td>对应的数据表</td>
</tr>
<tr>
<td>CATEGORY</td>
<td>VARCHAR(100)</td>
<td>项目种类</td>
</tr>
<tr>
<td>UNITNAME</td>
<td>VARCHAR(100)</td>
<td>项目测量单位</td>
</tr>
<tr>
<td>PARAM_TYPE</td>
<td>VARCHAR(30)</td>
<td>记录数据的类型  a date, a number, a text field</td>
</tr>
<tr>
<td>CONCEPTID</td>
<td>INT</td>
<td>-</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="d_labitems" tid="tid-KiS2xd" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>2</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>5</i></b></span><b class="dev__developer"><span class="dev__title">d_labitems</span></b></h2></span>
<blockquote>
<p>化验项目代码索引</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>LABEL</td>
<td>VARCHAR(100)</td>
<td>项目标签</td>
</tr>
<tr>
<td>FLUID</td>
<td>VARCHAR(100)</td>
<td>测量的物质 ‘blood’ ‘urine’</td>
</tr>
<tr>
<td>CATEGORY</td>
<td>VARCHAR(100)</td>
<td>测量的种类</td>
</tr>
<tr>
<td>LOINC_CODE</td>
<td>VARCHAR(100)</td>
<td>-</td>
</tr>
</tbody>
</table>
<span title-type="h1" class="header__span" style="transform:scale(1.0);"><h1 id="患者基本信息和院内采集信息数据" tid="tid-Q5CQPS" class="header__dev"><span style=""><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>0</i></b></span><b class="dev__developer"><span class="dev__title">患者基本信息和院内采集信息数据</span></b></h1></span>
<blockquote>
<p>患者基本信息和院内采集信息数据，共包含21个数据表</p>
</blockquote>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="admissions" tid="tid-4k22JW" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>1</i></b></span><b class="dev__developer"><span class="dev__title">admissions</span></b></h2></span>
<blockquote>
<p>患者入院情况</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name 	Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID 	INT</td>
<td>行号</td>
</tr>
<tr>
<td>SUBJECT_ID 	INT</td>
<td>患者编号</td>
</tr>
<tr>
<td>HADM_ID 	INT</td>
<td>病案号</td>
</tr>
<tr>
<td>ADMITTIME 	TIMESTAMP(0)</td>
<td>入院时间</td>
</tr>
<tr>
<td>DISCHTIME 	TIMESTAMP(0)</td>
<td>出院时间</td>
</tr>
<tr>
<td>DEATHTIME 	TIMESTAMP(0)</td>
<td>死亡时间</td>
</tr>
<tr>
<td>ADMISSION_TYPE 	VARCHAR(50)</td>
<td>入院类型</td>
</tr>
<tr>
<td>ADMISSION_LOCATION 	VARCHAR(50)</td>
<td>入院地点</td>
</tr>
<tr>
<td>DISCHARGE_LOCATION 	VARCHAR(50)</td>
<td>出院地点</td>
</tr>
<tr>
<td>INSURANCE 	VARCHAR(255)</td>
<td>保险类型</td>
</tr>
<tr>
<td>LANGUAGE 	VARCHAR(10)</td>
<td>语种</td>
</tr>
<tr>
<td>RELIGION 	VARCHAR(50)</td>
<td>宗教信仰</td>
</tr>
<tr>
<td>MARITAL_STATUS 	VARCHAR(50)</td>
<td>婚姻状况</td>
</tr>
<tr>
<td>ETHNICITY 	VARCHAR(200)</td>
<td>种族</td>
</tr>
<tr>
<td>EDREGTIME 	TIMESTAMP(0)</td>
<td>急诊留观登记时间</td>
</tr>
<tr>
<td>EDOUTTIME 	TIMESTAMP(0)</td>
<td>急诊留观出观时间</td>
</tr>
<tr>
<td>DIAGNOSIS 	VARCHAR(300)</td>
<td>初步诊断</td>
</tr>
<tr>
<td>HOSPITAL_EXPIRE_FLAG 	TINYINT</td>
<td>院内死亡标记</td>
</tr>
<tr>
<td>HAS_CHARTEVENTS_DATA 	TINYINT</td>
<td>是否有chartevents记录</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="callout" tid="tid-xBF2bW" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>2</i></b></span><b class="dev__developer"><span class="dev__title">callout</span></b></h2></span>
<blockquote>
<p>患者ICU出科的即时信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name 	Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID 	INT</td>
<td>行号</td>
</tr>
<tr>
<td>SUBJECT_ID 	INT</td>
<td>患者编号</td>
</tr>
<tr>
<td>HADM_ID 	INT</td>
<td>病案号</td>
</tr>
<tr>
<td>SUBMIT_WARDID 	INT</td>
<td>提交申请的科室代码</td>
</tr>
<tr>
<td>SUBMIT_CAREUNIT 	VARCHAR(15)</td>
<td>提交申请的科室所属的ICU cost类型</td>
</tr>
<tr>
<td>CURR_WARDID 	INT</td>
<td>患者所属科室</td>
</tr>
<tr>
<td>CURR_CAREUNIT 	VARCHAR(15)</td>
<td>患者所属的ICU cost类型</td>
</tr>
<tr>
<td>CALLOUT_WARDID 	INT</td>
<td>申请转移的地方 0 代表 Home / 1 代表转移到可用的的病房</td>
</tr>
<tr>
<td>CALLOUT_SERVICE 	VARCHAR(10)</td>
<td>患者需接受的治疗服务</td>
</tr>
<tr>
<td>REQUEST_TELE 	SMALLINT</td>
<td>预防患者已经感染的疾病</td>
</tr>
<tr>
<td>REQUEST_RESP 	SMALLINT</td>
<td>预防患者已经感染的疾病</td>
</tr>
<tr>
<td>REQUEST_CDIFF 	SMALLINT</td>
<td>预防患者已经感染的疾病</td>
</tr>
<tr>
<td>REQUEST_MRSA 	SMALLINT</td>
<td>预防患者已经感染的疾病</td>
</tr>
<tr>
<td>REQUEST_VRE 	SMALLINT</td>
<td>预防患者已经感染的疾病</td>
</tr>
<tr>
<td>CALLOUT_STATUS 	VARCHAR(20)</td>
<td>申请的状态</td>
</tr>
<tr>
<td>CALLOUT_OUTCOME 	VARCHAR(20)</td>
<td>‘Discharged’ or ‘Cancelled’</td>
</tr>
<tr>
<td>DISCHARGE_WARDID 	INT</td>
<td>实际转移的地方 0 代表 Home / 1 代表转移到可用的的病房</td>
</tr>
<tr>
<td>ACKNOWLEDGE_STATUS 	VARCHAR(20)</td>
<td>申请的反馈结果状态  ‘Acknowledged’, ‘Revised’, ‘Unacknowledged’ or ‘Reactivated’</td>
</tr>
<tr>
<td>CREATETIME 	TIMESTAMP(0)</td>
<td>申请创建时间</td>
</tr>
<tr>
<td>UPDATETIME 	TIMESTAMP(0)</td>
<td>更新时间</td>
</tr>
<tr>
<td>ACKNOWLEDGETIME 	TIMESTAMP(0)</td>
<td>反馈时间</td>
</tr>
<tr>
<td>OUTCOMETIME 	TIMESTAMP(0)</td>
<td>callout完成时间</td>
</tr>
<tr>
<td>FIRSTRESERVATIONTIME 	TIMESTAMP(0)</td>
<td>首次病房保留时间</td>
</tr>
<tr>
<td>CURRENTRESERVATIONTIME 	TIMESTAMP(0)</td>
<td>当前病房保留时间</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="caregivers" tid="tid-74AJEx" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>3</i></b></span><b class="dev__developer"><span class="dev__title">caregivers</span></b></h2></span>
<blockquote>
<p>护理人员信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name 	Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID 	INT</td>
<td>行号</td>
</tr>
<tr>
<td>CGID 	INT</td>
<td>护理人员标志符</td>
</tr>
<tr>
<td>LABEL 	VARCHAR(15)</td>
<td>护理人员的头衔 RN, MD, PharmD</td>
</tr>
<tr>
<td>DESCRIPTION 	VARCHAR(30)</td>
<td>护理人员的结构化数据信息 17 unique values</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="chartevents" tid="tid-hfBXDT" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>4</i></b></span><b class="dev__developer"><span class="dev__title">chartevents</span></b></h2></span>
<blockquote>
<p>患者观察记录数据</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>In CareVue</th>
<th>In Metavision</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>Y</td>
<td>Y</td>
<td>行号</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>NUMBER(7,0)</td>
<td>Y</td>
<td>Y</td>
<td>患者编号</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>NUMBER(7,0)</td>
<td>Y</td>
<td>Y</td>
<td>病案号</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>NUMBER(7,0)</td>
<td>Y</td>
<td>Y</td>
<td>ICU病案号</td>
</tr>
<tr>
<td>ITEMID</td>
<td>NUMBER(7,0)</td>
<td>Y</td>
<td>Y</td>
<td>项目标识符</td>
</tr>
<tr>
<td>CHARTTIME</td>
<td>DATE</td>
<td>Y</td>
<td>Y</td>
<td>记录时间</td>
</tr>
<tr>
<td>STORETIME</td>
<td>DATE</td>
<td>Y</td>
<td>Y</td>
<td>存储时间</td>
</tr>
<tr>
<td>CGID</td>
<td>NUMBER(7,0)</td>
<td>Y</td>
<td>Y</td>
<td>护理人员标识符</td>
</tr>
<tr>
<td>VALUE</td>
<td>VARCHAR2(200 BYTE)</td>
<td>Y</td>
<td>Y</td>
<td>项目测量的值</td>
</tr>
<tr>
<td>VALUENUM</td>
<td>NUMBER</td>
<td>Y</td>
<td>Y</td>
<td>项目测量的数字信息</td>
</tr>
<tr>
<td>VALUEUOM</td>
<td>VARCHAR2(20 BYTE)</td>
<td>Y</td>
<td>Y</td>
<td>项目测量的值对应的单位</td>
</tr>
<tr>
<td>WARNING</td>
<td>NUMBER(1,0)</td>
<td></td>
<td>Y</td>
<td>测量过程发生的警告 / Metavision specific columns</td>
</tr>
<tr>
<td>ERROR</td>
<td>NUMBER(1,0)</td>
<td></td>
<td>Y</td>
<td>测量过程发生的错误 / Metavision specific columns</td>
</tr>
<tr>
<td>RESULTSTATUS</td>
<td>VARCHAR2(20 BYTE)</td>
<td>Y</td>
<td></td>
<td>测量类型 ‘Manual’ or ‘Automatic’ /  CareVue specific columns</td>
</tr>
<tr>
<td>STOPPED</td>
<td>VARCHAR2(20 BYTE)</td>
<td>Y</td>
<td></td>
<td>测量是否停止</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="cptevents" tid="tid-teiRQF" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>5</i></b></span><b class="dev__developer"><span class="dev__title">cptevents</span></b></h2></span>
<blockquote>
<p>患者操作记录，记录程序操作是对哪位患者收费，便于知道某种操作是否执行</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>行号</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>患者编号</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>病案号</td>
</tr>
<tr>
<td>COSTCENTER</td>
<td>VARCHAR(10)</td>
<td>操作部门</td>
</tr>
<tr>
<td>CHARTDATE</td>
<td>TIMESTAMP(0)</td>
<td>操作时间</td>
</tr>
<tr>
<td>CPT_CD</td>
<td>VARCHAR(10)</td>
<td>操作的原始编码code</td>
</tr>
<tr>
<td>CPT_NUMBER</td>
<td>INT</td>
<td>CPT_CD 的数字信息</td>
</tr>
<tr>
<td>CPT_SUFFIX</td>
<td>VARCHAR(5)</td>
<td>CPT_CD 的文本后缀</td>
</tr>
<tr>
<td>TICKET_ID_SEQ</td>
<td>INT</td>
<td>CPT_CD 的顺序</td>
</tr>
<tr>
<td>SECTIONHEADER</td>
<td>VARCHAR(50)</td>
<td>CPT_CD 的种类</td>
</tr>
<tr>
<td>SUBSECTIONHEADER</td>
<td>VARCHAR(300)</td>
<td>CPT_CD 的种类</td>
</tr>
<tr>
<td>DESCRIPTION</td>
<td>VARCHAR(200)</td>
<td>CPT_CD 的详细信息</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="datetimeevents" tid="tid-3Z4jJy" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>6</i></b></span><b class="dev__developer"><span class="dev__title">datetimeevents</span></b></h2></span>
<blockquote>
<p>患者操作时间信息，包括患者在ICU中所有时间的测量。</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>行号</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>患者编号</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>病案号</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>ICU病案号</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>项目标识符</td>
</tr>
<tr>
<td>CHARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>记录时间</td>
</tr>
<tr>
<td>STORETIME</td>
<td>TIMESTAMP(0)</td>
<td>存储时间</td>
</tr>
<tr>
<td>CGID</td>
<td>INT</td>
<td>护理人员标识符</td>
</tr>
<tr>
<td>VALUE</td>
<td>TIMESTAMP(0)</td>
<td>同上chartevents</td>
</tr>
<tr>
<td>VALUEUOM</td>
<td>VARCHAR(50)</td>
<td>同上chartevents</td>
</tr>
<tr>
<td>WARNING</td>
<td>SMALLINT</td>
<td>同上chartevents</td>
</tr>
<tr>
<td>ERROR</td>
<td>SMALLINT</td>
<td>同上chartevents</td>
</tr>
<tr>
<td>RESULTSTATUS</td>
<td>VARCHAR(50)</td>
<td>同上chartevents</td>
</tr>
<tr>
<td>STOPPED</td>
<td>VARCHAR(50)</td>
<td>同上chartevents</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="diagnoses_icd" tid="tid-eDRBfM" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>7</i></b></span><b class="dev__developer"><span class="dev__title">diagnoses_icd</span></b></h2></span>
<blockquote>
<p>患者诊断ICD-9编码</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>PostgreSQL data type</th>
<th>Modifiers</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>not null</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>not null</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>not null</td>
<td>-</td>
</tr>
<tr>
<td>SEQ_NUM</td>
<td>INT</td>
<td></td>
<td>ICD诊断顺序</td>
</tr>
<tr>
<td>ICD9_CODE</td>
<td>VARCHAR(10)</td>
<td></td>
<td>实际编码IDC-9</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="drgcodes" tid="tid-di24m7" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>8</i></b></span><b class="dev__developer"><span class="dev__title">drgcodes</span></b></h2></span>
<blockquote>
<p>患者诊断类别组，包含诊断所属的种类</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>PostgreSQL data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>DRG_TYPE</td>
<td>VARCHAR(20)</td>
<td>诊断类别</td>
</tr>
<tr>
<td>DRG_CODE</td>
<td>VARCHAR(20)</td>
<td>诊断编码</td>
</tr>
<tr>
<td>DESCRIPTION</td>
<td>VARCHAR(300)</td>
<td>详细描述</td>
</tr>
<tr>
<td>DRG_SEVERITY</td>
<td>SMALLINT</td>
<td>严重程度</td>
</tr>
<tr>
<td>DRG_MORTALITY</td>
<td>SMALLINT</td>
<td>死亡率</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="icustays" tid="tid-ePde6a" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>9</i></b></span><b class="dev__developer"><span class="dev__title">icustays</span></b></h2></span>
<blockquote>
<p>ICU入住信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>ICU病案号</td>
</tr>
<tr>
<td>DBSOURCE</td>
<td>VARCHAR(20)</td>
<td>来源数据库  ‘carevue’ ‘metavision’ 在某些地方处理上有所不同</td>
</tr>
<tr>
<td>FIRST_CAREUNIT</td>
<td>VARCHAR(20)</td>
<td>患者入住监护室24小时内的首个ICU监护室种类</td>
</tr>
<tr>
<td>LAST_CAREUNIT</td>
<td>VARCHAR(20)</td>
<td>患者入住监护室24小时内的最终ICU监护室种类</td>
</tr>
<tr>
<td>FIRST_WARDID</td>
<td>SMALLINT</td>
<td>监护室编号</td>
</tr>
<tr>
<td>LAST_WARDID</td>
<td>SMALLINT</td>
<td>监护室编号</td>
</tr>
<tr>
<td>INTIME</td>
<td>TIMESTAMP(0)</td>
<td>入科时间</td>
</tr>
<tr>
<td>OUTTIME</td>
<td>TIMESTAMP(0)</td>
<td>出科时间</td>
</tr>
<tr>
<td>LOS</td>
<td>DOUBLE</td>
<td>入住时长 可能包括单个或多个ICU单位</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="inputevents_cv" tid="tid-EthbkE" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>10</i></b></span><b class="dev__developer"><span class="dev__title">inputevents_cv</span></b></h2></span>
<blockquote>
<p>使用carevue监护系统记录的入量信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>CHARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>记录时间</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>项目标识符</td>
</tr>
<tr>
<td>AMOUNT</td>
<td>DOUBLE PRECISION</td>
<td>总入量</td>
</tr>
<tr>
<td>AMOUNTUOM</td>
<td>VARCHAR(30)</td>
<td>入量单位</td>
</tr>
<tr>
<td>RATE</td>
<td>DOUBLE PRECISION</td>
<td>给药速率</td>
</tr>
<tr>
<td>RATEUOM</td>
<td>VARCHAR(30)</td>
<td>速率单位</td>
</tr>
<tr>
<td>STORETIME</td>
<td>TIMESTAMP(0)</td>
<td>存储时间</td>
</tr>
<tr>
<td>CGID</td>
<td>BIGINT</td>
<td>护理人员编码</td>
</tr>
<tr>
<td>ORDERID</td>
<td>BIGINT</td>
<td>同一次输入的多个药物进行链接</td>
</tr>
<tr>
<td>LINKORDERID</td>
<td>BIGINT</td>
<td>同一次的单个药物不同改变进行链接</td>
</tr>
<tr>
<td>STOPPED</td>
<td>VARCHAR(30)</td>
<td>输入是否暂停</td>
</tr>
<tr>
<td>NEWBOTTLE</td>
<td>INT</td>
<td>新配制的溶液</td>
</tr>
<tr>
<td>ORIGINALAMOUNT</td>
<td>DOUBLE PRECISION</td>
<td>-</td>
</tr>
<tr>
<td>ORIGINALAMOUNTUOM</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
<tr>
<td>ORIGINALROUTE</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
<tr>
<td>ORIGINALRATE</td>
<td>DOUBLE PRECISION</td>
<td>-</td>
</tr>
<tr>
<td>ORIGINALRATEUOM</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
<tr>
<td>ORIGINALSITE</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="inputevents_mv" tid="tid-8ppPNr" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>11</i></b></span><b class="dev__developer"><span class="dev__title">inputevents_mv</span></b></h2></span>
<blockquote>
<p>使用metavision系统记录的入量信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>STARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>入量开始时间</td>
</tr>
<tr>
<td>ENDTIME</td>
<td>TIMESTAMP(0)</td>
<td>入量结束时间</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>项目标识符</td>
</tr>
<tr>
<td>AMOUNT</td>
<td>DOUBLE PRECISION</td>
<td>总入量</td>
</tr>
<tr>
<td>AMOUNTUOM</td>
<td>VARCHAR(30)</td>
<td>入量单位</td>
</tr>
<tr>
<td>RATE</td>
<td>DOUBLE PRECISION</td>
<td>给药速率</td>
</tr>
<tr>
<td>RATEUOM</td>
<td>VARCHAR(30)</td>
<td>速率单位</td>
</tr>
<tr>
<td>STORETIME</td>
<td>TIMESTAMP(0)</td>
<td>存储时间</td>
</tr>
<tr>
<td>CGID</td>
<td>BIGINT</td>
<td>护理人员编号</td>
</tr>
<tr>
<td>ORDERID</td>
<td>BIGINT</td>
<td>同上</td>
</tr>
<tr>
<td>LINKORDERID</td>
<td>BIGINT</td>
<td>同上</td>
</tr>
<tr>
<td>ORDERCATEGORYNAME</td>
<td>VARCHAR(100)</td>
<td>-</td>
</tr>
<tr>
<td>SECONDARYORDERCATEGORYNAME</td>
<td>VARCHAR(100)</td>
<td>-</td>
</tr>
<tr>
<td>ORDERCOMPONENTTYPEDESCRIPTION</td>
<td>VARCHAR(200)</td>
<td>-</td>
</tr>
<tr>
<td>ORDERCATEGORYDESCRIPTION</td>
<td>VARCHAR(50)</td>
<td>-</td>
</tr>
<tr>
<td>PATIENTWEIGHT</td>
<td>DOUBLE PRECISION</td>
<td>患者体重 (kg)</td>
</tr>
<tr>
<td>TOTALAMOUNT</td>
<td>DOUBLE PRECISION</td>
<td>溶液液体总量</td>
</tr>
<tr>
<td>TOTALAMOUNTUOM</td>
<td>VARCHAR(50)</td>
<td>溶液液体总量单位</td>
</tr>
<tr>
<td>ISOPENBAG</td>
<td>SMALLINT</td>
<td>-</td>
</tr>
<tr>
<td>CONTINUEINNEXTDEPT</td>
<td>SMALLINT</td>
<td>转移是否继续入量</td>
</tr>
<tr>
<td>CANCELREASON</td>
<td>SMALLINT</td>
<td>取消原因</td>
</tr>
<tr>
<td>STATUSDESCRIPTION</td>
<td>VARCHAR(30)</td>
<td>项目最终状态 changed paused finishedrunning stopped rewritten flushed</td>
</tr>
<tr>
<td>COMMENTS_STATUS</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
<tr>
<td>COMMENTS_TITLE</td>
<td>VARCHAR(100)</td>
<td>-</td>
</tr>
<tr>
<td>COMMENTS_DATE</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>ORIGINALAMOUNT</td>
<td>DOUBLE PRECISION</td>
<td>-</td>
</tr>
<tr>
<td>ORIGINALRATE</td>
<td>DOUBLE PRECISION</td>
<td>-</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="labevents" tid="tid-RAGGF5" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>12</i></b></span><b class="dev__developer"><span class="dev__title">labevents</span></b></h2></span>
<blockquote>
<p>患者化验项目</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>项目标识符</td>
</tr>
<tr>
<td>CHARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>测量时间</td>
</tr>
<tr>
<td>VALUE</td>
<td>VARCHAR(200)</td>
<td>测量项目</td>
</tr>
<tr>
<td>VALUENUM</td>
<td>DOUBLE PRECISION</td>
<td>测量数值数据</td>
</tr>
<tr>
<td>VALUEUOM</td>
<td>VARCHAR(20)</td>
<td>测量单位</td>
</tr>
<tr>
<td>FLAG</td>
<td>VARCHAR(20)</td>
<td>测量值是否异常</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="microbiologyevents" tid="tid-2A52kS" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>13</i></b></span><b class="dev__developer"><span class="dev__title">microbiologyevents</span></b></h2></span>
<blockquote>
<p>患者标本微生物病原体检测结果，包括采集的培养物和相关敏感性</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>CHARTDATE</td>
<td>TIMESTAMP(0)</td>
<td>记录日期</td>
</tr>
<tr>
<td>CHARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>记录时间</td>
</tr>
<tr>
<td>SPEC_ITEMID</td>
<td>INT</td>
<td>化验项目标识符</td>
</tr>
<tr>
<td>SPEC_TYPE_DESC</td>
<td>VARCHAR(100)</td>
<td>化验类型 血液 尿液 痰</td>
</tr>
<tr>
<td>ORG_ITEMID</td>
<td>INT</td>
<td>生成的有机物标识符</td>
</tr>
<tr>
<td>ORG_NAME</td>
<td>VARCHAR(100)</td>
<td>有机物名称</td>
</tr>
<tr>
<td>ISOLATE_NUM</td>
<td>SMALLINT</td>
<td>分离菌落数目</td>
</tr>
<tr>
<td>AB_ITEMID</td>
<td>INT</td>
<td>抗生素敏感性测试标识符</td>
</tr>
<tr>
<td>AB_NAME</td>
<td>VARCHAR(30)</td>
<td>抗生素名称</td>
</tr>
<tr>
<td>DILUTION_TEXT</td>
<td>VARCHAR(10)</td>
<td>测试抗生素敏感性</td>
</tr>
<tr>
<td>DILUTION_COMPARISON</td>
<td>VARCHAR(20)</td>
<td>-</td>
</tr>
<tr>
<td>DILUTION_VALUE</td>
<td>DOUBLE PRECISION</td>
<td>测试抗生素敏感性时的稀释值</td>
</tr>
<tr>
<td>INTERPRETATION</td>
<td>VARCHAR(5)</td>
<td>解释抗生素的敏感性和试验结果 “S”是敏感的，“R”是抗性的，“I”是中间的，“P”是待定的</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="noteevents" tid="tid-8jPFNx" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>14</i></b></span><b class="dev__developer"><span class="dev__title">noteevents</span></b></h2></span>
<blockquote>
<p>治疗记录</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>CHARTDATE</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>CHARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>STORETIME</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>CATEGORY</td>
<td>VARCHAR(50)</td>
<td>记录类型 ‘Discharge’ ：出院</td>
</tr>
<tr>
<td>DESCRIPTION</td>
<td>VARCHAR(300)</td>
<td>记录类别 ‘Summary’ ：总结</td>
</tr>
<tr>
<td>CGID</td>
<td>INT</td>
<td>护理人员标识符</td>
</tr>
<tr>
<td>ISERROR</td>
<td>CHAR(1)</td>
<td>‘1’ 代表该记录被标记为错误</td>
</tr>
<tr>
<td>TEXT</td>
<td>TEXT</td>
<td>医嘱内容</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="outputevents" tid="tid-yEyycB" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>15</i></b></span><b class="dev__developer"><span class="dev__title">outputevents</span></b></h2></span>
<blockquote>
<p>患者出量数据</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>CHARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>项目标识符</td>
</tr>
<tr>
<td>VALUE</td>
<td>DOUBLE PRECISION</td>
<td>出量值</td>
</tr>
<tr>
<td>VALUEUOM</td>
<td>VARCHAR(30)</td>
<td>出量值的单位</td>
</tr>
<tr>
<td>STORETIME</td>
<td>TIMESTAMP(0)</td>
<td>存储时间</td>
</tr>
<tr>
<td>CGID</td>
<td>BIGINT</td>
<td>护理人员标识符</td>
</tr>
<tr>
<td>STOPPED</td>
<td>VARCHAR(30)</td>
<td>是否中断</td>
</tr>
<tr>
<td>NEWBOTTLE</td>
<td>INT</td>
<td>是否有准备新溶液</td>
</tr>
<tr>
<td>ISERROR</td>
<td>SMALLINT</td>
<td>是否被标记为错误</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="patients" tid="tid-f8aKDW" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>16</i></b></span><b class="dev__developer"><span class="dev__title">patients</span></b></h2></span>
<blockquote>
<p>患者信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>患者编号</td>
</tr>
<tr>
<td>GENDER</td>
<td>VARCHAR(5)</td>
<td>性别</td>
</tr>
<tr>
<td>DOB</td>
<td>TIMESTAMP(0)</td>
<td>出生日期</td>
</tr>
<tr>
<td>DOD</td>
<td>TIMESTAMP(0)</td>
<td>死亡日期</td>
</tr>
<tr>
<td>DOD_HOSP</td>
<td>TIMESTAMP(0)</td>
<td>院内登记死亡日期</td>
</tr>
<tr>
<td>DOD_SSN</td>
<td>TIMESTAMP(0)</td>
<td>社保局登记死亡日期</td>
</tr>
<tr>
<td>EXPIRE_FLAG</td>
<td>VARCHAR(5)</td>
<td>死亡标记</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="prescriptions" tid="tid-M3YpMD" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>17</i></b></span><b class="dev__developer"><span class="dev__title">prescriptions</span></b></h2></span>
<blockquote>
<p>病人用药记录</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>STARTDATE</td>
<td>TIMESTAMP(0)</td>
<td>用药开始时间</td>
</tr>
<tr>
<td>ENDDATE</td>
<td>TIMESTAMP(0)</td>
<td>用药结束时间</td>
</tr>
<tr>
<td>DRUG_TYPE</td>
<td>VARCHAR(100)</td>
<td>药物类型</td>
</tr>
<tr>
<td>DRUG</td>
<td>VARCHAR(100)</td>
<td>药物名称</td>
</tr>
<tr>
<td>DRUG_NAME_POE</td>
<td>VARCHAR(100)</td>
<td>药物说明</td>
</tr>
<tr>
<td>DRUG_NAME_GENERIC</td>
<td>VARCHAR(100)</td>
<td>药物说明</td>
</tr>
<tr>
<td>FORMULARY_DRUG_CD</td>
<td>VARCHAR(120)</td>
<td>处方药代码</td>
</tr>
<tr>
<td>GSN</td>
<td>VARCHAR(200)</td>
<td>Generic Sequence Number</td>
</tr>
<tr>
<td>NDC</td>
<td>VARCHAR(120)</td>
<td>National Drug Code</td>
</tr>
<tr>
<td>PROD_STRENGTH</td>
<td>VARCHAR(120)</td>
<td>-</td>
</tr>
<tr>
<td>DOSE_VAL_RX</td>
<td>VARCHAR(120)</td>
<td>-</td>
</tr>
<tr>
<td>DOSE_UNIT_RX</td>
<td>VARCHAR(120)</td>
<td>-</td>
</tr>
<tr>
<td>FORM_VAL_DISP</td>
<td>VARCHAR(120)</td>
<td>-</td>
</tr>
<tr>
<td>FORM_UNIT_DISP</td>
<td>VARCHAR(120)</td>
<td>-</td>
</tr>
<tr>
<td>ROUTE</td>
<td>VARCHAR(120)</td>
<td>-</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="procedureevents_mv" tid="tid-skNrfW" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>18</i></b></span><b class="dev__developer"><span class="dev__title">procedureevents_mv</span></b></h2></span>
<blockquote>
<p>metavision系统操作信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT NOT NULL</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT NOT NULL</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT NOT NULL</td>
<td>-</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>STARTTIME</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>ENDTIME</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>ITEMID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>VALUE</td>
<td>DOUBLE PRECISION</td>
<td>-</td>
</tr>
<tr>
<td>VALUEUOM</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
<tr>
<td>LOCATION</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
<tr>
<td>LOCATIONCATEGORY</td>
<td>VARCHAR(30)</td>
<td>-</td>
</tr>
<tr>
<td>STORETIME</td>
<td>TIMESTAMP(0)</td>
<td>-</td>
</tr>
<tr>
<td>CGID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ORDERID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>LINKORDERID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ORDERCATEGORYNAME</td>
<td>VARCHAR(100)</td>
<td>药物一级分类名称</td>
</tr>
<tr>
<td>SECONDARYORDERCATEGORYNAME</td>
<td>VARCHAR(100)</td>
<td>药物二级分类名称</td>
</tr>
<tr>
<td>ORDERCATEGORYDESCRIPTION</td>
<td>VARCHAR(50)</td>
<td>药物分类描述</td>
</tr>
<tr>
<td>ISOPENBAG</td>
<td>SMALLINT</td>
<td>-</td>
</tr>
<tr>
<td>CONTINUEINNEXTDEPT</td>
<td>SMALLINT</td>
<td>-</td>
</tr>
<tr>
<td>CANCELREASON</td>
<td>SMALLINT</td>
<td>取消原因</td>
</tr>
<tr>
<td>STATUSDESCRIPTION</td>
<td>VARCHAR(30)</td>
<td>状态描述</td>
</tr>
<tr>
<td>COMMENTS_EDITEDBY</td>
<td>VARCHAR(30)</td>
<td></td>
</tr>
<tr>
<td>COMMENTS_CANCELEDBY</td>
<td>VARCHAR(30)</td>
<td></td>
</tr>
<tr>
<td>COMMENTS_DATE</td>
<td>TIMESTAMP(0)</td>
<td></td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="procedures_icd" tid="tid-KhxF2A" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>19</i></b></span><b class="dev__developer"><span class="dev__title">procedures_icd</span></b></h2></span>
<blockquote>
<p>病人手术记录ICD-9编码</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>PostgreSQL data type</th>
<th>Modifiers</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>not null</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>not null</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>not null</td>
<td>-</td>
</tr>
<tr>
<td>SEQ_NUM</td>
<td>INT</td>
<td></td>
<td>操作顺序</td>
</tr>
<tr>
<td>ICD9_CODE</td>
<td>VARCHAR(10)</td>
<td></td>
<td>ICD-9 编码</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="services" tid="tid-fjrsmy" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>20</i></b></span><b class="dev__developer"><span class="dev__title">services</span></b></h2></span>
<blockquote>
<p>患者需要接受的医疗服务</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>TRANSFERTIME</td>
<td>TIMESTAMP(0)</td>
<td>服务种类更改时间</td>
</tr>
<tr>
<td>PREV_SERVICE</td>
<td>VARCHAR(20)</td>
<td>前次服务种类</td>
</tr>
<tr>
<td>CURR_SERVICE</td>
<td>VARCHAR(20)</td>
<td>当前服务种类</td>
</tr>
</tbody>
</table>
<hr>
<span title-type="h3" class="header__span" style="transform:scale(0.8);left: -74.00px;"><h3 id="服务的名称缩写及其详细说明" tid="tid-YTMmHQ" class="header__dev"><span style="visibility: hidden;"><b class="dev__fe"><i>1</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>0</i></b></span><span class="iconfont icon-weibiaoti22 titleIcon" style="left: 32.00px;"></span><b class="dev__developer"><span class="dev__title">服务的名称缩写及其详细说明</span></b></h3></span>
<table>
<thead>
<tr>
<th>Service</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>CMED</td>
<td>Cardiac Medical - for non-surgical cardiac related admissions</td>
</tr>
<tr>
<td>CSURG</td>
<td>Cardiac Surgery - for surgical cardiac admissions</td>
</tr>
<tr>
<td>DENT</td>
<td>Dental - for dental/jaw related admissions</td>
</tr>
<tr>
<td>ENT</td>
<td>Ear, nose, and throat - conditions primarily affecting these areas</td>
</tr>
<tr>
<td>GU</td>
<td>Genitourinary - reproductive organs/urinary system</td>
</tr>
<tr>
<td>GYN</td>
<td>Gynecological - female reproductive systems and breasts</td>
</tr>
<tr>
<td>MED</td>
<td>Medical - general service for internal medicine</td>
</tr>
<tr>
<td>NB</td>
<td>Newborn - infants born at the hospital</td>
</tr>
<tr>
<td>NBB</td>
<td>Newborn baby - infants born at the hospital</td>
</tr>
<tr>
<td>NMED</td>
<td>Neurologic Medical - non-surgical, relating to the brain</td>
</tr>
<tr>
<td>NSURG</td>
<td>Neurologic Surgical - surgical, relating to the brain</td>
</tr>
<tr>
<td>OBS</td>
<td>Obstetrics - conerned with childbirth and the care of women giving birth</td>
</tr>
<tr>
<td>ORTHO</td>
<td>Orthopaedic - surgical, relating to the musculoskeletal system</td>
</tr>
<tr>
<td>OMED</td>
<td>Orthopaedic medicine - non-surgical, relating to musculoskeletal system</td>
</tr>
<tr>
<td>PSURG</td>
<td>Plastic - restortation/reconstruction of the human body (including cosmetic or aesthetic)</td>
</tr>
<tr>
<td>PSYCH</td>
<td>Psychiatric - mental disorders relating to mood, behaviour, cognition, or perceptions</td>
</tr>
<tr>
<td>SURG</td>
<td>Surgical - general surgical service not classified elsewhere</td>
</tr>
<tr>
<td>TRAUM</td>
<td>Trauma - injury or damage caused by physical harm from an external source</td>
</tr>
<tr>
<td>TSURG</td>
<td>Thoracic Surgical - surgery on the thorax, located between the neck and the abdomen</td>
</tr>
<tr>
<td>VSURG</td>
<td>Vascular Surgical - surgery relating to the circulatory system</td>
</tr>
</tbody>
</table>
<span title-type="h2" class="header__span" style="transform:scale(0.9);left: -37.00px;"><h2 id="transfers" tid="tid-KEKZbQ" class="header__dev"><span style="position: relative;left: -5px;"><b class="dev__fe"><i>3</i></b><span class="dev__slash">|</span><b class="dev__ux"><i>21</i></b></span><b class="dev__developer"><span class="dev__title">transfers</span></b></h2></span>
<blockquote>
<p>患者周转信息</p>
</blockquote>
<table>
<thead>
<tr>
<th>Name</th>
<th>Postgres data type</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>ROW_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>SUBJECT_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>HADM_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>ICUSTAY_ID</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>DBSOURCE</td>
<td>VARCHAR(20)</td>
<td>数据来源  ‘carevue’  ‘metavision’</td>
</tr>
<tr>
<td>EVENTTYPE</td>
<td>VARCHAR(20)</td>
<td>转移的类型 ‘admit’  ‘transfer’  ‘discharge’</td>
</tr>
<tr>
<td>PREV_CAREUNIT</td>
<td>VARCHAR(20)</td>
<td>前次所在监护室</td>
</tr>
<tr>
<td>CURR_CAREUNIT</td>
<td>VARCHAR(20)</td>
<td>当前所在监护室</td>
</tr>
<tr>
<td>PREV_WARDID</td>
<td>SMALLINT</td>
<td>前次所在科室代码</td>
</tr>
<tr>
<td>CURR_WARDID</td>
<td>SMALLINT</td>
<td>当前所在科室代码</td>
</tr>
<tr>
<td>INTIME</td>
<td>TIMESTAMP(0)</td>
<td>入科时间</td>
</tr>
<tr>
<td>OUTTIME</td>
<td>TIMESTAMP(0)</td>
<td>出科时间</td>
</tr>
<tr>
<td>LOS</td>
<td>INT</td>
<td>住院时长</td>
</tr>
</tbody>
</table>

<br><p class="essaySuffix-eof">__EOF__</p><div class="essaySuffix-box"><div class="essaySuffix-box-left"><img src="https://files-cdn.cnblogs.com/files/linzhenyu/ico.bmp" alt=""></div><div class="essaySuffix-box-right"><span class="essaySuffix-right-title">本文作者</span>：<strong><span style="font-size: 12px;"><a href="https://www.cnblogs.com/linzhenyu/p/13206761.html" target="_blank">林震宇</a></span></strong> <br><span style="font-weight: bold; white-space:nowrap;">本文链接</span>：<a href="https://www.cnblogs.com/linzhenyu/p/13206761.html" target="_blank">https://www.cnblogs.com/linzhenyu/p/13206761.html</a><br><span class="essaySuffix-right-title">关于博主</span>：评论和私信会在第一时间回复。或者<a href="https://msg.cnblogs.com/msg/send/linzhenyu" target="_blank">直接私信</a>我。<br><span class="essaySuffix-right-title">版权声明</span>：本博客所有文章除特别声明外，均采用 <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" alt="BY-NC-SA" title="BY-NC-SA" target="_blank">BY-NC-SA</a> 许可协议。转载请注明出处！<br><span class="essaySuffix-right-title">声援博主</span>：如果您觉得文章对您有帮助，可以点击文章右下角<strong><span style="color: #ff0000; font-size: 12pt;">【<a id="post-up" onclick="votePost(13206761,'Digg')" href="javascript:void(0);">推荐</a>】</span></strong>一下。您的鼓励是博主的最大动力！<br></div><div style="clear: both;"></div></div></div>
<div id="MySignature"></div>
<div class="clear"></div>
<div id="blog_post_info_block"><div id="BlogPostCategory">
    分类: 
            <a href="https://www.cnblogs.com/linzhenyu/category/1802468.html" target="_blank"><span class="iconfont icon-marketing_fill"></span>知识发现与数据挖掘</a></div>
<div id="EntryTag">
    标签: 
            <a href="https://www.cnblogs.com/linzhenyu/tag/MIMIC/"><span class="iconfont icon-label_fill"></span>MIMIC</a>,             <a href="https://www.cnblogs.com/linzhenyu/tag/KDD/"><span class="iconfont icon-label_fill"></span>KDD</a>,             <a href="https://www.cnblogs.com/linzhenyu/tag/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/"><span class="iconfont icon-label_fill"></span>数据挖掘</a></div>

    <div id="blog_post_info">
<div id="green_channel">
        <a href="javascript:void(0);" id="green_channel_digg" onclick="DiggIt(13206761,cb_blogId,1);green_channel_success(this,'谢谢推荐！');">好文要顶</a>
        <a id="green_channel_follow" onclick="follow('731d7b80-4ed9-444d-6c9c-08d810f32599');" href="javascript:void(0);">关注我</a>
    <a id="green_channel_favorite" onclick="AddToWz(cb_entryId);return false;" href="javascript:void(0);">收藏该文</a>
    <a id="green_channel_weibo" href="javascript:void(0);" title="分享至新浪微博" onclick="ShareToTsina()"><img src="https://common.cnblogs.com/images/icon_weibo_24.png" alt=""></a>
    <a id="green_channel_wechat" href="javascript:void(0);" title="分享至微信" onclick="shareOnWechat()"><img src="https://common.cnblogs.com/images/wechat.png" alt=""></a>
</div>
<div id="author_profile">
    <div id="author_profile_info" class="author_profile_info">
            <a href="https://home.cnblogs.com/u/linzhenyu/" target="_blank"><img src="https://pic.cnblogs.com/face/2067563/20200705212727.png" class="author_avatar" alt=""></a>
        <div id="author_profile_detail" class="author_profile_info">
            <a href="https://home.cnblogs.com/u/linzhenyu/">林震宇</a><br>
            <a href="https://home.cnblogs.com/u/linzhenyu/followees/">关注 - 3</a><br>
            <a href="https://home.cnblogs.com/u/linzhenyu/followers/">粉丝 - 11</a>
        </div>
    </div>
    <div class="clear"></div>
    <div id="author_profile_honor"></div>
    <div id="author_profile_follow">
                <a href="javascript:void(0);" onclick="follow('731d7b80-4ed9-444d-6c9c-08d810f32599');return false;">+加关注</a>
    </div>
</div>
<div id="div_digg">
    <div class="diggit" onclick="votePost(13206761,'Digg')">
        <span class="diggnum" id="digg_count">0</span>
    </div>
    <div class="buryit" onclick="votePost(13206761,'Bury')">
        <span class="burynum" id="bury_count">0</span>
    </div>
    <div class="clear"></div>
    <div class="diggword" id="digg_tips">
    </div>
</div>

<script type="text/javascript">
    currentDiggType = 0;
</script></div>
    <div class="clear"></div>
    <div id="post_next_prev">

    <a href="https://www.cnblogs.com/linzhenyu/p/13205481.html" class="p_n_p_prefix">« </a> 上一篇：    <a href="https://www.cnblogs.com/linzhenyu/p/13205481.html" title="发布于 2020-06-28 22:47">Python 函数</a>
    <br>
    <a href="https://www.cnblogs.com/linzhenyu/p/13212481.html" class="p_n_p_prefix">» </a> 下一篇：    <a href="https://www.cnblogs.com/linzhenyu/p/13212481.html" title="发布于 2020-06-30 10:50">KDD MIMIC-III 数据分析，预处理和可视化</a>

</div>
</div>
            </div>
            <div class="postDesc" style="display: block;">posted @ 
<span id="post-date">2020-06-29 10:55</span>&nbsp;
<a href="https://www.cnblogs.com/linzhenyu/">林震宇</a>&nbsp;
阅读(<span id="post_view_count">947</span>)&nbsp;
评论(<span id="post_comment_count">0</span>)&nbsp;
<a href="https://i.cnblogs.com/EditPosts.aspx?postid=13206761" rel="nofollow">编辑</a>&nbsp;
<a href="javascript:void(0)" onclick="AddToWz(13206761);return false;">收藏</a></div>
        </div>
	    
	    
    </div><!--end: topics 文章、评论容器-->
</div>
<script src="https://common.cnblogs.com/highlight/10.3.1/highlight.min.js"></script>
<script>markdown_highlight();</script>
<script>
    var allowComments = true, cb_blogId = 611063, cb_blogApp = 'linzhenyu', cb_blogUserGuid = '731d7b80-4ed9-444d-6c9c-08d810f32599';
    var cb_entryId = 13206761, cb_entryCreatedDate = '2020-06-29 10:55', cb_postType = 1;
    updatePostStats(
        [cb_entryId],
        function(id, count) { $("#post_view_count").text(count) },
        function(id, count) { $("#post_comment_count").text(count) })
</script>
<a name="!comments"></a>
<div id="blog-comments-placeholder"></div>
<div id="comment_form" class="commentform">
    <a name="commentform"></a>
    <div id="divCommentShow"></div>
    <div id="comment_nav"><span id="span_refresh_tips"></span><a href="javascript:void(0);" onclick="return RefreshCommentList();" id="lnk_RefreshComments" runat="server" clientidmode="Static">刷新评论</a><a href="#" onclick="return RefreshPage();">刷新页面</a><a href="#top">返回顶部</a></div>
    <div id="comment_form_container" style="visibility: visible;"><script type="text/javascript" src="https://mention.cnblogs.com/bundles/mention.min.js"></script>
<div id="commentform_title">发表评论</div>
<span id="tip_comment" style="color:Red"></span>
<div class="commentbox_main comment_textarea">
    <div class="commentbox_title">
        <div class="commentbox_title_left">
            <span id="btn_edit_comment" class="commentbox_tab active" title="编辑评论">编辑</span>
            <span id="btn_preview_comment" class="commentbox_tab" title="Markdown 预览">预览</span>
        </div>
        <div class="commentbox_title_right">
            <span id="ubb_bold" class="comment_icon" alt="粗体" title="添加粗体(Ctrl + B)">
                <svg class="comment_svg" version="1.1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <g fill-rule="evenodd">
                        <path d="m13.221 19c1.4414 0 2.5793-0.27451 3.3759-0.82353 0.92931-0.66667 1.4034-1.7059 1.4034-3.1176 0-0.94118-0.22759-1.7059-0.66379-2.2549-0.45517-0.56863-1.119-0.94118-2.0103-1.1176 0.68276-0.27451 1.1948-0.64706 1.5552-1.1569 0.36034-0.54902 0.55-1.2157 0.55-2 0-1.0588-0.36034-1.902-1.0621-2.5294-0.75862-0.66667-1.8207-1-3.1672-1h-6.2017v14h6.2207zm-0.82196-8h-3.3987v-4h3.4367c0.91139 0 1.557 0.15686 1.9747 0.47059 0.37975 0.29412 0.58861 0.78431 0.58861 1.451 0 0.72549-0.20886 1.2549-0.58861 1.5882-0.39873 0.31373-1.0633 0.4902-2.0127 0.4902zm0.52612 6h-3.9249v-4h3.9855c1.052 0 1.8208 0.16216 2.3064 0.48649 0.46532 0.32432 0.70809 0.84685 0.70809 1.5856 0 0.72072-0.3237 1.2252-0.9711 1.5495-0.50578 0.25225-1.2139 0.37838-2.104 0.37838z" fill-rule="nonzero" stroke-width=".35"></path>
                    </g>
                </svg>
            </span>
            <span id="ubb_url" class="comment_icon" title="添加链接(Ctrl + K)" alt="链接">
                <svg class="comment_svg comment_svg_stroke" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <g fill-rule="evenodd">
                        <g transform="translate(4 4)" fill-rule="nonzero" stroke-width=".4">
                            <path d="m6.304 9.696c-0.288-0.288-0.512-0.608-0.704-0.992-0.16-0.32-0.032-0.704 0.288-0.864 0.32-0.16 0.704-0.032 0.864 0.288 0.128 0.224 0.256 0.448 0.448 0.64 0.928 0.928 2.432 0.928 3.36 0l3.36-3.328c0.928-0.928 0.928-2.432 0-3.36s-2.432-0.928-3.36 0l-2.272 2.272c-0.256 0.256-0.64 0.256-0.896 0-0.256-0.256-0.256-0.64 0-0.896l2.272-2.272c1.44-1.44 3.744-1.44 5.184 0 1.44 1.44 1.44 3.744 0 5.184l-3.36 3.296c-0.704 0.704-1.632 1.088-2.592 1.088-0.928 0-1.856-0.352-2.592-1.056z"></path>
                            <path d="m3.776 15.808c-0.992 0-1.888-0.384-2.592-1.056-1.44-1.44-1.44-3.744 0-5.184l3.328-3.328c1.44-1.44 3.744-1.44 5.184 0 0.288 0.288 0.544 0.64 0.736 1.024 0.16 0.32 0 0.704-0.32 0.864-0.32 0.16-0.704 0-0.864-0.32-0.128-0.256-0.288-0.48-0.48-0.672-0.928-0.928-2.432-0.928-3.36 0l-3.296 3.328c-0.928 0.928-0.928 2.432 0 3.36 0.448 0.448 1.056 0.704 1.664 0.704 0.608 0 1.248-0.256 1.664-0.704l2.112-2.112c0.256-0.256 0.64-0.256 0.896 0s0.256 0.64 0 0.896l-2.112 2.112c-0.672 0.704-1.568 1.088-2.56 1.088z"></path>
                        </g>
                    </g>
                </svg>
            </span>
            <span id="ubb_code" class="comment_icon" title="添加代码(Ctrl + `)" alt="代码">
                <svg class="comment_svg comment_svg_stroke" version="1.1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <g fill-rule="evenodd">
                        <g transform="translate(16 6)" stroke-linecap="round" stroke-width="2">
                            <line x1=".5" x2="4.5" y1=".7" y2="6.3"></line>
                            <line transform="translate(2.5 9.1) scale(1 -1) translate(-2.5 -9.1)" x1=".5" x2="4.5" y1="6.3" y2="11.9"></line>
                        </g>
                        <g transform="translate(3 6.1)" stroke-linecap="round" stroke-width="2">
                            <line transform="translate(2.5 3.5) scale(-1 1) translate(-2.5 -3.5)" x1=".5" x2="4.5" y1=".7" y2="6.3"></line>
                            <line transform="translate(2.5 9.1) scale(-1) translate(-2.5 -9.1)" x1=".5" x2="4.5" y1="6.3" y2="11.9"></line>
                        </g>
                        <path transform="translate(12 12.5) scale(1 -1) translate(-12 -12.5)" d="m10.778 7.1249c0.50008-0.11366 0.9978 0.16911 1.1643 0.64128l0.032406 0.11223 2 8.8c0.1224 0.53855-0.21496 1.0744-0.75351 1.1968-0.50008 0.11366-0.9978-0.16911-1.1643-0.64128l-0.032406-0.11223-2-8.8c-0.1224-0.53855 0.21496-1.0744 0.75351-1.1968z" fill-rule="nonzero" stroke-width=".25"></path>
                    </g>
                </svg>
            </span>
            <span id="ubb_quote" class="comment_icon" title="添加引用(Ctrl + Q)" alt="引用">
                <svg class="comment_svg" version="1.1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <g fill-rule="evenodd">
                        <g transform="translate(5 4)" fill-rule="nonzero" stroke-width=".25">
                            <path d="m5.0013 15v-5.2702h-2.8008c-0.13413-3.3762 1.2004-6.2143 4.0009-8.5135l-1.2-1.2163c-3.335 2.2996-5.0013 5.8119-5.0013 10.54v4.4595h5.0013-1.285e-5zm8.7987 0v-5.2702h-2.8008c-0.13453-3.3762 1.2-6.2143 4.0009-8.5135l-1.2-1.2163c-3.335 2.2996-5.0013 5.8119-5.0013 10.54v4.4595h5.0013-1.28e-5z"></path>
                        </g>
                    </g>
                </svg>
            </span>
            <span id="ubb_img" class="comment_icon" alt="图片" title="上传图片(Ctrl + I)">
                <svg class="comment_svg" version="1.1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <g fill-rule="evenodd">
                        <g transform="translate(3 3.8)" fill-rule="nonzero">
                            <path d="m14.1 0.58235h-11.2c-1.32 0-2.4 1.0482-2.4 2.3294v10.871c0 1.2812 1.08 2.3294 2.4 2.3294h11.2c1.32 0 2.4-1.0482 2.4-2.3294v-10.871c0-1.2812-1.08-2.3294-2.4-2.3294zm0.7 13.569-3.63-3.4165 1.33-1.2909c0.21-0.20382 0.59-0.20382 0.8 0l1.6 1.5529v2.7856c0 0.13588-0.04 0.26206-0.1 0.36882zm-11.9-12.016h11.2c0.44 0 0.8 0.34941 0.8 0.77647v5.8915l-0.47-0.45618c-0.84-0.825-2.22-0.825-3.07 0l-1.35 1.3103-2.39-2.2421c-0.85-0.825-2.22-0.825-3.05-0.019412l-2.48 2.2615v-6.7456c0.01-0.42706 0.37-0.77647 0.81-0.77647zm-0.8 11.647v-1.9897l3.6-3.2806c0.21-0.20382 0.58-0.21353 0.81 0.0097059l6.43 6.0371h-10.04c-0.44 0-0.8-0.33971-0.8-0.77647z"></path>
                            <ellipse cx="10.5" cy="6.4059" rx="1" ry="1"></ellipse>
                        </g>
                    </g>
                </svg>
            </span>
        </div>
    </div>
    <div style="display:none">
        <span id="comment_edit_id"></span>
        <span id="span_parentcomment_id"></span>
        <span id="span_parent_id"></span>
        <span id="span_comment_replyto"></span>
        <span id="span_comment_posted"></span>
        <span id="span_current_user_id">18be4a65-8603-4113-8c9f-08d6b3fcf9d2</span>
    </div>
    <textarea id="tbCommentBody" placeholder="支持 Markdown"></textarea>
    <div id="tbCommentBodyPreview" class="feedbackCon" style="display: none">
        <div id="tbCommentBodyPreviewBody" class="blog_comment_body comment_preview cnblogs-markdown"></div>
    </div>
    <div class="commentbox_footer">
        <a class="comment_option">Markdown 帮助</a>
        <span id="btn_comment_options" class="comment_option">
            <input id="ubb_auto_completion" class="inline_middle" type="checkbox">
            <label class="inline_middle" for="ubb_auto_completion">自动补全</label>
        </span>
    </div>
</div>
<p id="commentbox_opt">
    <input id="btn_comment_submit" type="button" class="comment_btn" title="提交评论(Ctrl + Enter)" value="提交评论">
    <span id="span_comment_canceledit" style="display:none"><a href="javascript:void(0);" onclick="return CancelCommentEdit()">不改了</a></span>
    <a href="javascript:void(0);" onclick="return logout();">退出</a>
            <a id="commentbox_opt_sub" href="javascript:void(0);" title="订阅后有新评论时会邮件通知您" onclick="commentManager.Subscribe()">订阅评论</a>
            <a href="//www.cnblogs.com/memoryLost/" target="_blank">我的博客</a>
</p>
<div id="tip_comment2" style="color:Red"></div>
<p>[Ctrl+Enter快捷键提交]</p>
<script>var commentEditor = initCommentEditor("tbCommentBody");</script>

</div>
    <div class="ad_text_commentbox" id="ad_text_under_commentbox"></div>
    <div id="ad_t2"></div>
    <div id="opt_under_post"></div>
    <div id="cnblogs_c1" class="c_ad_block">
        <div id="div-gpt-ad-1592365906576-0" style="width: 300px; height: 250px;"></div>
    </div>
    <div id="under_post_news"></div>
    <div id="cnblogs_c2" class="c_ad_block">
        <div id="div-gpt-ad-1592366332455-0" style="width: 468px; height: 60px;"></div>
    </div>
    <div id="under_post_kb"></div>
    <div id="HistoryToday" class="c_ad_block"></div>
    <script type="text/javascript">
       var commentManager = new blogCommentManager();
       commentManager.renderComments(0);
       fixPostBody();
       deliverBigBanner();
setTimeout(function() { incrementViewCount(cb_entryId); }, 50);       deliverT2();
       deliverC1C2();
       loadNewsAndKb();
       loadBlogSignature();
LoadPostCategoriesTags(cb_blogId, cb_entryId);       LoadPostInfoBlock(cb_blogId, cb_entryId, cb_blogApp, cb_blogUserGuid);
       GetPrevNextPost(cb_entryId, cb_blogId, cb_entryCreatedDate, cb_postType);
       loadOptUnderPost();
       GetHistoryToday(cb_blogId, cb_blogApp, cb_entryCreatedDate);
   </script>
</div>

	</div><!--end: forFlow -->
	</div><!--end: mainContent 主体内容容器-->
	<div id="sideBar">
		<div id="sideBarMain">
			<div id="sidebar_news" class="newsItem"><!--done-->
<h3 class="catListTitle">公告</h3>

<div id="blog-news"><div class="container">    <div class="menu-wrap optiscroll is-enabled" id="menuWrap" style="display:none"><div class=" optiscroll-content" style="right: -2px; bottom: -2px;">        <nav class="menu">            <!-- 个人简介 -->            <div class="introduce-box">                <div class="introduce-head">                    <div class="introduce-via" id="menuBlogAvatar"><img src="https://files-cdn.cnblogs.com/files/linzhenyu/ico.bmp"></div>                </div>                <div id="introduce">
        昵称：
        <a href="https://home.cnblogs.com/u/linzhenyu/">
            林震宇
        </a>
        <br>
        园龄：
        <a href="https://home.cnblogs.com/u/linzhenyu/" title="入园时间：2020-06-15">
            7个月
        </a>
        <br>
        粉丝：
        <a href="https://home.cnblogs.com/u/linzhenyu/followers/">
            11
        </a>
        <br>
        关注：
        <a href="https://home.cnblogs.com/u/linzhenyu/followees/">
            3
        </a>
        <div id="p_b_follow">
<a href="javascript:void(0)" onclick="follow('731d7b80-4ed9-444d-6c9c-08d810f32599')">+加关注</a></div>
        
    </div>            </div>            <!-- 导航 -->            <div class="nav-title"></div>            <div class="icon-list">                <ul id="m-nav-list">                <li><a href="https://www.cnblogs.com/linzhenyu/" target="_self">首页</a></li><li><a href="https://msg.cnblogs.com/send/linzhenyu" target="_blank">联系</a></li><li><a href="https://www.cnblogs.com/linzhenyu/rss" target="_blank">订阅</a></li><li><a href="https://i.cnblogs.com/" target="_blank">管理</a></li><li><a href="https://github.com/linzhenyuyuchen/" target="_blank">Github</a></li><li><a href="https://linzhenyuyuchen.github.io/" target="_blank">LZY Blog</a></li></ul>            </div>            <!-- 日历 -->            <span id="calendar-box"><div id="blog-calendar" style="visibility: visible;">

<table id="blogCalendar" class="Cal" cellspacing="0" cellpadding="0" title="Calendar" border="0">
    <tbody>
        <tr>
            <td colspan="7">
                <table class="CalTitle" cellspacing="0" border="0">
                    <tbody>
                        <tr>
                            <td class="CalNextPrev">
                                <a href="javascript:void(0);" onclick="loadBlogCalendar('2020/12/19'); return false;">&lt;</a>
                            </td>
                            <td align="center">2021年1月</td>
                            <td align="right" class="CalNextPrev">
                                <a href="javascript:void(0);" onclick="loadBlogCalendar('2021/02/19'); return false;">&gt;</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    <tr>
        <th class="CalDayHeader" align="center" abbr="日" scope="col">日</th>
        <th class="CalDayHeader" align="center" abbr="一" scope="col">一</th>
        <th class="CalDayHeader" align="center" abbr="二" scope="col">二</th>
        <th class="CalDayHeader" align="center" abbr="三" scope="col">三</th>
        <th class="CalDayHeader" align="center" abbr="四" scope="col">四</th>
        <th class="CalDayHeader" align="center" abbr="五" scope="col">五</th>
        <th class="CalDayHeader" align="center" abbr="六" scope="col">六</th>
    </tr>
            <tr>
                            <td class="CalOtherMonthDay" align="center">27</td>
                            <td class="CalOtherMonthDay" align="center">28</td>
                            <td class="CalOtherMonthDay" align="center">29</td>
                            <td class="CalOtherMonthDay" align="center">30</td>
                            <td class="CalOtherMonthDay" align="center">31</td>
                        <td class="" align="center">
                            1
                        </td>
                    <td class="CalWeekendDay" align="center">
                        2
                    </td>
            </tr>
                <tr>
                        <td class="CalWeekendDay" align="center">
                            3
                        </td>
                            <td class="" align="center">
                                4
                            </td>
                            <td class="" align="center">
                                5
                            </td>
                            <td class="" align="center">
                                6
                            </td>
                            <td class="" align="center">
                                7
                            </td>
                            <td class="" align="center">
                                8
                            </td>
                        <td class="CalWeekendDay" align="center">
                            <a href="https://www.cnblogs.com/linzhenyu/archive/2021/01/09.html"><u>9</u></a>
                        </td>
                </tr>
                <tr>
                        <td class="CalWeekendDay" align="center">
                            10
                        </td>
                            <td class="" align="center">
                                <a href="https://www.cnblogs.com/linzhenyu/archive/2021/01/11.html"><u>11</u></a>
                            </td>
                            <td class="" align="center">
                                12
                            </td>
                            <td class="" align="center">
                                13
                            </td>
                            <td class="" align="center">
                                14
                            </td>
                            <td class="" align="center">
                                <a href="https://www.cnblogs.com/linzhenyu/archive/2021/01/15.html"><u>15</u></a>
                            </td>
                        <td class="CalWeekendDay" align="center">
                            16
                        </td>
                </tr>
                <tr>
                        <td class="CalWeekendDay" align="center">
                            17
                        </td>
                            <td class="" align="center">
                                18
                            </td>
                            <td class="CalTodayDay" align="center">
                                19
                            </td>
                            <td class="" align="center">
                                20
                            </td>
                            <td class="" align="center">
                                21
                            </td>
                            <td class="" align="center">
                                22
                            </td>
                        <td class="CalWeekendDay" align="center">
                            23
                        </td>
                </tr>
                <tr>
                        <td class="CalWeekendDay" align="center">
                            24
                        </td>
                            <td class="" align="center">
                                25
                            </td>
                            <td class="" align="center">
                                26
                            </td>
                            <td class="" align="center">
                                27
                            </td>
                            <td class="" align="center">
                                28
                            </td>
                            <td class="" align="center">
                                29
                            </td>
                        <td class="CalWeekendDay" align="center">
                            30
                        </td>
                </tr>
                <tr>
                        <td class="CalWeekendDay" align="center">
                            31
                        </td>
                            <td class="CalOtherMonthDay" align="center">
                                1
                            </td>
                            <td class="CalOtherMonthDay" align="center">
                                2
                            </td>
                            <td class="CalOtherMonthDay" align="center">
                                3
                            </td>
                            <td class="CalOtherMonthDay" align="center">
                                4
                            </td>
                            <td class="CalOtherMonthDay" align="center">
                                5
                            </td>
                        <td class="CalOtherMonthDay" align="center">
                            6
                        </td>
                </tr>
    </tbody>
</table></div></span>            <!-- 找找看 -->            <div class="m-list-title" style="display: block;"><span>找找看</span></div>            <div class="m-icon-list" id="sb-sidebarSearchBox"><div id="sb_widget_my_zzk" class="div_my_zzk"><input id="q" type="text" onkeydown="return zzk_go_enter(event);" class="input_my_zzk"></div></div>            <!-- 积分与排名 -->            <div class="m-list-title" style="display: block;"><span>积分排名<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-sidebarScorerank"><div><ul><li><a href="javascript:void(0);"><span class="iconfont icon-collection_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>积分 -	
9110</a></li><li><a href="javascript:void(0);"><span class="iconfont icon-collection_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>排名 -	
91408</a></li></ul></div></div>            <!-- 最新随笔 -->            <div class="m-list-title" style="display: block;"><span>最新随笔<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-sidebarRecentposts"><div><ul><li><a href="https://www.cnblogs.com/linzhenyu/p/14283274.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>【医学图像处理】提取勾画</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/14282712.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>【Kaggle】HuBMAP - 图像分割竞赛</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/14261697.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>【Kaggle】 冠军方案 SIIM-ACR Pneumothorax Segmentation</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/14261667.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>【图像分割 损失函数】Loss functions for image segmentation</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/14254625.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>【批处理】子文件夹压缩包和指定后缀名文件</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/14110873.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>RIADD (ISBI-2021)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/14063779.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>SegPC2021</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13600454.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>自然语言处理工具之gensim / 预训练模型 word2vec doc2vec</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13591294.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Linux 根目录空间不足解决方法</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13578360.html"><span class="iconfont icon-time_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>文本挖掘预处理之分词 / 向量化 / TF-IDF / Hash trick 附代码 Demo</a></li></ul></div></div>            <!-- 我的标签 -->            <div class="m-list-title" style="display: block;"><span>我的标签<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-toptags"><div><ul><li><a href="https://www.cnblogs.com/linzhenyu/tag/Linux/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Linux(22)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/Python/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Python(11)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/KDD/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>KDD(8)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>数据挖掘(8)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>图像分割(7)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/%E8%AE%BA%E6%96%87/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>论文(7)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/NLP/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>NLP(7)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/%E5%AE%9E%E4%BE%8B%E5%88%86%E5%89%B2/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>实例分割(6)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>自然语言处理(5)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>深度学习(5)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/tag/"><span class="iconfont icon-label_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>更多</a></li></ul></div></div>            <!-- 随笔分类 -->            <div class="m-list-title" style="display: block;"><span>随笔分类<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-classify"><div><ul><li><a href="https://www.cnblogs.com/linzhenyu/category/1834642.html" rel="" target=""><span class="iconfont icon-marketing_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Kaggle(3)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/category/1802477.html" rel="" target=""><span class="iconfont icon-marketing_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Linux(8)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/category/1802475.html" rel="" target=""><span class="iconfont icon-marketing_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Python(12)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/category/1802472.html" rel="" target=""><span class="iconfont icon-marketing_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>论文笔记(7)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/category/1802470.html" rel="" target=""><span class="iconfont icon-marketing_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>图像分割(7)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/category/1802468.html" rel="" target=""><span class="iconfont icon-marketing_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>知识发现与数据挖掘(10)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/category/1834638.html" rel="" target=""><span class="iconfont icon-marketing_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>自然语言处理(4)</a></li></ul></div></div>            <!-- 文章分类 -->            <div class="m-list-title"><span>文章分类<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-ArticleCategory"></div>            <!-- 阅读排行 -->            <div class="m-list-title" style="display: block;"><span>阅读排行<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-topview"><div><ul><li><a href="https://www.cnblogs.com/linzhenyu/p/13277552.html"><span class="iconfont icon-browse_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Torchtext使用教程 文本数据处理 (1779)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13229431.html"><span class="iconfont icon-browse_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>KDD MIMIC-IV与MIMIC-III的区别(982)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13206761.html"><span class="iconfont icon-browse_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>KDD MIMIC-III数据集介绍(947)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13212481.html"><span class="iconfont icon-browse_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>KDD MIMIC-III 数据分析，预处理和可视化(387)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13591294.html"><span class="iconfont icon-browse_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Linux 根目录空间不足解决方法(359)</a></li></ul></div></div>            <!-- 推荐排行 -->            <div class="m-list-title" style="display: block;"><span>推荐排行<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-topDiggPosts"><div><ul><li><a href="https://www.cnblogs.com/linzhenyu/p/13591294.html"><span class="iconfont icon-like_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Linux 根目录空间不足解决方法(1)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13428285.html"><span class="iconfont icon-like_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Ubuntu安装postgresql / psycopg2包 / Python连接postgreSQL(1)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13297132.html"><span class="iconfont icon-like_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>自监督 论文 Self-supervised Visual Feature Learning with Deep Neural Networks(1)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13277552.html"><span class="iconfont icon-like_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Torchtext使用教程 文本数据处理 (1)</a></li></ul></div></div>            <!-- 最新评论 -->            <div class="m-list-title" style="display: block;"><span>最新评论<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-recentComments"><div><ul><li><a href="https://www.cnblogs.com/linzhenyu/p/13591294.html"><span class="iconfont icon-pinglunzu" style="color: #888;font-size: 15px;margin-right: 5px;"></span>Re:Linux 根目录空间不足解决方法</a><div style="padding-left: 1.5em;color: #777;position: relative;top: -5px;">真不错
</div><div style="text-align: right;color: #444;position: relative;top: -10px;">--达芬骑驴</div></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13277552.html"><span class="iconfont icon-pinglunzu" style="color: #888;font-size: 15px;margin-right: 5px;"></span>Re:Torchtext使用教程 文本数据处理</a><div style="padding-left: 1.5em;color: #777;position: relative;top: -5px;">博主博客好漂亮，要是写个 配置教程就好了
</div><div style="text-align: right;color: #444;position: relative;top: -10px;">--douzujun</div></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13229431.html"><span class="iconfont icon-pinglunzu" style="color: #888;font-size: 15px;margin-right: 5px;"></span>Re:KDD MIMIC-IV与MIMIC-III的区别</a><div style="padding-left: 1.5em;color: #777;position: relative;top: -5px;">博主您好！我想问下您，这个MIMIC IV数据库是如何申请的？或者说申请途径有哪些？
</div><div style="text-align: right;color: #444;position: relative;top: -10px;">--Zero0Alpha</div></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13169082.html"><span class="iconfont icon-pinglunzu" style="color: #888;font-size: 15px;margin-right: 5px;"></span>Re:Python 基础知识点</a><div style="padding-left: 1.5em;color: #777;position: relative;top: -5px;">写的太好了，马上会用python了，希望马上看到下一篇！
</div><div style="text-align: right;color: #444;position: relative;top: -10px;">--Tanglement</div></li><li><a href="https://www.cnblogs.com/linzhenyu/p/13156301.html"><span class="iconfont icon-pinglunzu" style="color: #888;font-size: 15px;margin-right: 5px;"></span>Re:Linux 文件打包与解压缩</a><div style="padding-left: 1.5em;color: #777;position: relative;top: -5px;">太多了，记不住。只会一个tar -zxvf file.tar.gz
</div><div style="text-align: right;color: #444;position: relative;top: -10px;">--Tanglement</div></li></ul></div></div>            <!-- 文章档案 -->            <div class="m-list-title"><span>文章档案<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-articlearchive"></div>            <!-- 随笔档案 -->            <div class="m-list-title" style="display: block;"><span>随笔档案<span class="iconfont icon-select m-list-title-select"></span></span></div>            <div class="m-icon-list" id="sb-record"><div><ul><li><a href="https://www.cnblogs.com/linzhenyu/archive/2021/01.html" rel="" target=""><span class="iconfont icon-task_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>2021年1月(5)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/archive/2020/12.html" rel="" target=""><span class="iconfont icon-task_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>2020年12月(1)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/archive/2020/11.html" rel="" target=""><span class="iconfont icon-task_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>2020年11月(1)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/archive/2020/09.html" rel="" target=""><span class="iconfont icon-task_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>2020年9月(1)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/archive/2020/08.html" rel="" target=""><span class="iconfont icon-task_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>2020年8月(7)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/archive/2020/07.html" rel="" target=""><span class="iconfont icon-task_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>2020年7月(17)</a></li><li><a href="https://www.cnblogs.com/linzhenyu/archive/2020/06.html" rel="" target=""><span class="iconfont icon-task_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>2020年6月(23)</a></li></ul></div></div>            <!-- 自定义列表 -->            <span id="menuCustomList"><div class="m-list-title" style="display: block;"><span>基友们</span></div><div class="m-icon-list"><div><ul><li><a href="https://www.cnblogs.com/chenshaowei/"><span class="iconfont icon-brush_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>Tanglement</a></li><li><a href="https://www.cnblogs.com/beeblog72/"><span class="iconfont icon-brush_fill" style="color: #888;font-size: 14px;margin-right: 5px;"></span>达芬骑驴</a></li></ul></div></div></span>        </nav>        <button class="close-button" id="close-button">Close Menu</button>        <div class="morph-shape" id="morph-shape" data-morph-open="M-7.312,0H15c0,0,66,113.339,66,399.5C81,664.006,15,800,15,800H-7.312V0z;M-7.312,0H100c0,0,0,113.839,0,400c0,264.506,0,400,0,400H-7.312V0z">            <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 100 800" preserveAspectRatio="none">                <path d="M-7.312,0H0c0,0,0,113.839,0,400c0,264.506,0,400,0,400h-7.312V0z"></path>            <desc>Created with Snap</desc><defs></defs></svg>        </div>    </div><div class="optiscroll-v"><b class="optiscroll-vtrack"></b></div><div class="optiscroll-h"><b class="optiscroll-htrack"></b></div></div>    <button class="menu-button" id="open-button">MENU</button>    <div class="content-wrap" id="content-wrap"></div><!-- /content-wrap --></div><div class="main-header" style="height: 40vh; background: url(&quot;https://cdn.jsdelivr.net/gh/BNDong/Cnblogs-Theme-SimpleMemory@master/img/webp/nothome_top_bg.webp&quot;) center center / cover no-repeat rgb(34, 34, 34);">    <canvas id="notHomeTopCanvas" width="0" height="0"></canvas>    <div class="vertical">        <div class="main-header-content inner" style="max-width: 100vw;">            <h1 class="page-title" id="homeTopTitle" style="display: none;">林震宇</h1>            <h2 class="page-description" id="hitokoto"></h2>            <h3 class="page-author" id="hitokotoAuthor"></h3>            <h1 class="sb-title" id="sbTitle">
    KDD MIMIC-III数据集介绍
    


</h1>            <p class="article-info" id="articleInfo"><p class="article-info-text"><span class="postMeta"><i class="iconfont icon-time1"></i>发表于 2020-06-29 10:55<i class="iconfont icon-browse"></i>阅读：947<i class="iconfont icon-interactive"></i>评论：0<i class="iconfont icon-hot"></i>推荐：0</span></p><a href="https://www.cnblogs.com/linzhenyu/category/1802468.html" target="_blank"><span class="article-info-tag article-tag-class-color">知识发现与数据挖掘</span></a><a href="https://www.cnblogs.com/linzhenyu/tag/MIMIC/" target="_blank"><span class="article-info-tag article-tag-color">MIMIC</span></a><a href="https://www.cnblogs.com/linzhenyu/tag/KDD/" target="_blank"><span class="article-info-tag article-tag-color">KDD</span></a><a href="https://www.cnblogs.com/linzhenyu/tag/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/" target="_blank"><span class="article-info-tag article-tag-color">数据挖掘</span></a></p>        </div>    </div>    <a class="scroll-down" href="javascript:void(0);" data-offset="-45" style="display: none;">        <span class="hidden">Scroll Down</span>        <i class="scroll-down-icon iconfont icon-fanhui"></i>    </a></div><div id="loading" style="display: none;"></div><div id="bottomProgressBar"><div id="top-progress-bar" style="position: relative; top: 0px; left: 0px; right: 0px; background-color: rgb(119, 182, 255); height: 2px; width: 0%; transition: width 0.2s ease 0s, opacity 0.6s ease 0s; opacity: 1;"></div></div><div id="rightMenu"><div id="rightDashang" clickflg="false"><span class="rightMenuSpan rightDanshanSpan"><div class="ds-pay"><div class="ds-alipay"><img src="https://blog-static.cnblogs.com/files/linzhenyu/alipay.gif"><span>Alipay</span></div></div></span><i class="iconfont icon-shang"></i></div><div id="rightDiggit" clickflg="false" onclick="votePost(13206761,'Digg')"><span class="rightMenuSpan rightDiggitSpan">0</span><i class="iconfont icon-zan1"></i></div><div id="rightBuryit" clickflg="false" onclick="votePost(13206761,'Bury')"><span class="rightMenuSpan rightBuryitSpan">0</span><i class="iconfont icon-buzan"></i></div><div id="attention" onclick="follow('731d7b80-4ed9-444d-6c9c-08d810f32599')" clickflg="false"><span class="rightMenuSpan attentionSpan">关注</span><i class="iconfont icon-dianzan"></i></div><div id="toUpDown" data="down"><span class="rightMenuSpan toUpDownSpan">跳至底部</span><div id="toUpDownI" style="transform: rotate(-180deg); transform-origin: 50% 50%;"><i class="iconfont icon-zhiding"></i></div></div></div>
    <script type="text/javascript">window['__document_write_ajax_callbacks__']['4']();</script><script type="text/javascript">window['__document_write_ajax_callbacks__']['1']();</script>
<script type="text/javascript">window['__document_write_ajax_callbacks__']['5']();</script><script type="text/javascript">window['__document_write_ajax_callbacks__']['6']();</script><script>window['__document_write_ajax_callbacks__']['2']();</script>
    <div id="profile_block">
        昵称：
        <a href="https://home.cnblogs.com/u/linzhenyu/">
            林震宇
        </a>
        <br>
        园龄：
        <a href="https://home.cnblogs.com/u/linzhenyu/" title="入园时间：2020-06-15">
            7个月
        </a>
        <br>
        粉丝：
        <a href="https://home.cnblogs.com/u/linzhenyu/followers/">
            11
        </a>
        <br>
        关注：
        <a href="https://home.cnblogs.com/u/linzhenyu/followees/">
            3
        </a>
        <div id="p_b_follow">
<a href="javascript:void(0)" onclick="follow('731d7b80-4ed9-444d-6c9c-08d810f32599')">+加关注</a></div>
        <script type="text/javascript">window['__document_write_ajax_callbacks__']['7']();</script><script>window['__document_write_ajax_callbacks__']['3']();</script>
    </div>
</div>

</div>
<div id="sidebar_c3"></div>
			<script>loadBlogDefaultCalendar();</script>			
			<div id="leftcontentcontainer">
				<div id="blog-sidecolumn"><!-- 搜索 -->
<div id="sidebar_search" class="sidebar-block">
    <div id="sidebar_search" class="mySearch">
        <h3 class="catListTitle">搜索</h3>
        <div id="sidebar_search_box">
            <div id="widget_my_zzk" class="div_my_zzk">
                <input type="text" id="q" onkeydown="return zzk_go_enter(event);" class="input_my_zzk">&nbsp;<input onclick="zzk_go()" type="button" value="找找看" id="btnZzk" class="btn_my_zzk">
            </div>
            
        </div>
    </div>
</div>

<!-- 常用链接 -->
<div id="sidebar_shortcut" class="sidebar-block"><div class="catListLink">
<h3 class="catListTitle">
常用链接
</h3>
<ul>
    
<li><a href="https://www.cnblogs.com/linzhenyu/p/" title="我的博客的随笔列表">我的随笔</a></li>
<li><a href="https://www.cnblogs.com/linzhenyu/MyComments.html" title="我的发表过的评论列表">我的评论</a></li>
<li><a href="https://www.cnblogs.com/linzhenyu/OtherPosts.html" title="我评论过的随笔列表">我的参与</a></li>
<li><a href="https://www.cnblogs.com/linzhenyu/RecentComments.html" title="我的博客的评论列表">最新评论</a></li>
<li><a href="https://www.cnblogs.com/linzhenyu/tag/" title="我的博客的标签列表">我的标签</a></li>

</ul>
</div>

</div>

<!-- 最新随笔 -->
<div id="sidebar_recentposts" class="sidebar-block"><div class="catListEssay">
<h3 class="catListTitle">最新随笔</h3>
    <ul>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/14283274.html">1.【医学图像处理】提取勾画</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/14282712.html">2.【Kaggle】HuBMAP - 图像分割竞赛</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/14261697.html">3.【Kaggle】 冠军方案 SIIM-ACR Pneumothorax Segmentation</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/14261667.html">4.【图像分割 损失函数】Loss functions for image segmentation</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/14254625.html">5.【批处理】子文件夹压缩包和指定后缀名文件</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/14110873.html">6.RIADD (ISBI-2021)</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/14063779.html">7.SegPC2021</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/13600454.html">8.自然语言处理工具之gensim / 预训练模型 word2vec doc2vec </a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/13591294.html">9.Linux 根目录空间不足解决方法</a>

                </li>
                <li>
                    
<a href="https://www.cnblogs.com/linzhenyu/p/13578360.html">10.文本挖掘预处理之分词 / 向量化 / TF-IDF / Hash trick 附代码 Demo</a>

                </li>
    </ul>
</div>

</div>

<!-- 我的标签 -->
<div id="sidebar_toptags" class="sidebar-block"><div class="catListTag">
<h3 class="catListTitle">我的标签</h3>
<ul>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/Linux/">Linux<span class="tag-count">(22)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/Python/">Python<span class="tag-count">(11)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/KDD/">KDD<span class="tag-count">(8)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/">数据挖掘<span class="tag-count">(8)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2/">图像分割<span class="tag-count">(7)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/%E8%AE%BA%E6%96%87/">论文<span class="tag-count">(7)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/NLP/">NLP<span class="tag-count">(7)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/%E5%AE%9E%E4%BE%8B%E5%88%86%E5%89%B2/">实例分割<span class="tag-count">(6)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86/">自然语言处理<span class="tag-count">(5)</span></a>
        </li>
        <li>
            <a href="https://www.cnblogs.com/linzhenyu/tag/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/">深度学习<span class="tag-count">(5)</span></a>
        </li>
    <li>
        <a href="https://www.cnblogs.com/linzhenyu/tag/">更多</a>
    </li>

</ul>
</div>

</div>

<!-- 积分与排名 -->
<div id="sidebar_scorerank" class="sidebar-block"><div class="catListBlogRank">
<h3 class="catListTitle">积分与排名</h3>
<ul>
	<li class="liScore">
		积分 -	
9110
	</li>
	<li class="liRank">
		排名 -	
91408
	</li>
</ul>
</div>



</div>

<!-- 随笔分类、随笔档案、文章分类、新闻分类、相册、链接 -->
<div id="sidebar_categories">

    <div id="sidebar_postcategory" class="catListPostCategory sidebar-block">
        <h3 class="catListTitle">
            
随笔分类



        </h3>

        <ul>

                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/category/1834642.html" rel="" target="">
    Kaggle(3)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/category/1802477.html" rel="" target="">
    Linux(8)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/category/1802475.html" rel="" target="">
    Python(12)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/category/1802472.html" rel="" target="">
    论文笔记(7)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/category/1802470.html" rel="" target="">
    图像分割(7)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/category/1802468.html" rel="" target="">
    知识发现与数据挖掘(10)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/category/1834638.html" rel="" target="">
    自然语言处理(4)
</a>
 

                </li>                
            
        </ul>


    </div>    
    <div id="sidebar_postarchive" class="catListPostArchive sidebar-block">
        <h3 class="catListTitle">
            
随笔档案



        </h3>

        <ul>

                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/archive/2021/01.html" rel="" target="">
    2021年1月(5)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/archive/2020/12.html" rel="" target="">
    2020年12月(1)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/archive/2020/11.html" rel="" target="">
    2020年11月(1)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/archive/2020/09.html" rel="" target="">
    2020年9月(1)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/archive/2020/08.html" rel="" target="">
    2020年8月(7)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/archive/2020/07.html" rel="" target="">
    2020年7月(17)
</a>
 

                </li>                
                <li data-category-list-item-visible="true" style="display: block">
                    
<a href="https://www.cnblogs.com/linzhenyu/archive/2020/06.html" rel="" target="">
    2020年6月(23)
</a>
 

                </li>                
            
        </ul>


    </div>    
</div>

<!-- 最新评论 -->
<div id="sidebar_recentcomments" class="sidebar-block"><div class="catListComment">
<h3 class="catListTitle">最新评论</h3>

	<div class="RecentCommentBlock">
        <ul>
                    <li class="recent_comment_title"><a href="https://www.cnblogs.com/linzhenyu/p/13591294.html">1. Re:Linux 根目录空间不足解决方法</a></li>
                    <li class="recent_comment_body"><p>真不错</p>
</li>
                    <li class="recent_comment_author">--达芬骑驴</li>
                    <li class="recent_comment_title"><a href="https://www.cnblogs.com/linzhenyu/p/13277552.html">2. Re:Torchtext使用教程 文本数据处理 </a></li>
                    <li class="recent_comment_body"><p>博主博客好漂亮，要是写个 配置教程就好了</p>
</li>
                    <li class="recent_comment_author">--douzujun</li>
                    <li class="recent_comment_title"><a href="https://www.cnblogs.com/linzhenyu/p/13229431.html">3. Re:KDD MIMIC-IV与MIMIC-III的区别</a></li>
                    <li class="recent_comment_body"><p>博主您好！我想问下您，这个MIMIC IV数据库是如何申请的？或者说申请途径有哪些？</p>
</li>
                    <li class="recent_comment_author">--Zero0Alpha</li>
                    <li class="recent_comment_title"><a href="https://www.cnblogs.com/linzhenyu/p/13169082.html">4. Re:Python 基础知识点</a></li>
                    <li class="recent_comment_body"><p>写的太好了，马上会用python了，希望马上看到下一篇！</p>
</li>
                    <li class="recent_comment_author">--Tanglement</li>
                    <li class="recent_comment_title"><a href="https://www.cnblogs.com/linzhenyu/p/13156301.html">5. Re:Linux 文件打包与解压缩</a></li>
                    <li class="recent_comment_body"><p>太多了，记不住。只会一个tar -zxvf file.tar.gz</p>
</li>
                    <li class="recent_comment_author">--Tanglement</li>
        </ul>
    </div>
</div>

</div>


<!-- 阅读排行榜 -->
<div id="sidebar_topviewedposts" class="sidebar-block"><div class="catListView">
<h3 class="catListTitle">阅读排行榜</h3>
	<div id="TopViewPostsBlock">
        <ul style="word-break:break-all">
                    <li>
                        <a href="https://www.cnblogs.com/linzhenyu/p/13277552.html">
                            1. Torchtext使用教程 文本数据处理 (1779)
                        </a>
                    </li>
                    <li>
                        <a href="https://www.cnblogs.com/linzhenyu/p/13229431.html">
                            2. KDD MIMIC-IV与MIMIC-III的区别(982)
                        </a>
                    </li>
                    <li>
                        <a href="https://www.cnblogs.com/linzhenyu/p/13206761.html">
                            3. KDD MIMIC-III数据集介绍(947)
                        </a>
                    </li>
                    <li>
                        <a href="https://www.cnblogs.com/linzhenyu/p/13212481.html">
                            4. KDD MIMIC-III 数据分析，预处理和可视化(387)
                        </a>
                    </li>
                    <li>
                        <a href="https://www.cnblogs.com/linzhenyu/p/13591294.html">
                            5. Linux 根目录空间不足解决方法(359)
                        </a>
                    </li>
        </ul>
    </div>
</div>

</div>

<!-- 评论排行榜 -->


<!-- 推荐排行榜 -->
<div id="sidebar_topdiggedposts" class="sidebar-block">
<div id="topdigg_posts_wrap">
    <div class="catListView">
        <h3 class="catListTitle">推荐排行榜</h3>
        <div id="TopDiggPostsBlock">
            <ul style="word-break: break-all">
                        <li>
                            <a href="https://www.cnblogs.com/linzhenyu/p/13591294.html">
                                1. Linux 根目录空间不足解决方法(1)
                            </a>
                        </li>
                        <li>
                            <a href="https://www.cnblogs.com/linzhenyu/p/13428285.html">
                                2. Ubuntu安装postgresql / psycopg2包 / Python连接postgreSQL(1)
                            </a>
                        </li>
                        <li>
                            <a href="https://www.cnblogs.com/linzhenyu/p/13297132.html">
                                3. 自监督 论文 Self-supervised Visual Feature Learning with Deep Neural Networks(1)
                            </a>
                        </li>
                        <li>
                            <a href="https://www.cnblogs.com/linzhenyu/p/13277552.html">
                                4. Torchtext使用教程 文本数据处理 (1)
                            </a>
                        </li>
            </ul>
        </div>
    </div>
</div></div></div>
                    <script>loadBlogSideColumn();</script>
			</div>			
		</div><!--end: sideBarMain -->
	</div><!--end: sideBar 侧边栏容器 -->
	<div class="clear"></div>
	</div><!--end: main -->
	<div class="clear"></div>
	<div id="footer"><footer><footer-background><figure class="clouds"></figure><figure class="background"></figure><figure class="foreground"></figure></footer-background></footer><div class="footer-box"><div><span id="blogRunTimeSpan">This blog has running : 218 d 8 h 12 m 45 s</span><span class="my-face">ღゝ◡╹)ノ♡</span></div><div id="blogrollInfo">友情链接：<a href="https://www.cnblogs.com/beeblog72" target="_blank">达芬骑驴</a><span style="margin: 0 3px;">/</span><a href="https://linzhenyuyuchen.github.io/" target="_blank">LZY Blog</a><span style="margin: 0 3px;">/</span><a href="https://www.cnblogs.com/chenshaowei/" target="_blank">Tanglement</a></div><div>
		
Copyright © 2021 林震宇
Powered by .NET 5.0 on Kubernetes



	</div><div id="cnzzInfo"></div><div id="themeInfo">Theme version: <a href="https://github.com/BNDong/Cnblogs-Theme-SimpleMemory/tree/v1.3.1" target="_blank" style="color: #888;text-decoration: underline;">v1.3.1</a> / Loading theme version: <a href="https://github.com/BNDong/Cnblogs-Theme-SimpleMemory/tree/v1.3.1" target="_blank" style="color: #888;text-decoration: underline;">v1.3.1</a></div></div></div><!--end: footer -->
</div>