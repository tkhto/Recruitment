<template>
  <div class="create-position">
      <div class="container">
        <header>发布职位</header>
        <div class="form-wrapper">
            <el-form :model="PositionRequire" ref="PositionRequireForm" label-width="100px" class="demo-ruleForm">
                <el-form-item
                    label="职位名称"
                    :rules="[
                        { required: true, message: '名称不能为空'}
                    ]"
                >
                    <el-input type="text" v-model.number="PositionRequire.PositionName" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item
                    label="职位薪资"
                    :rules="[
                        { required: true, message: '薪资不能为空'}
                    ]"
                >   
                    <el-tooltip class="item" effect="dark" content="例：10-20。以K（千）为单位" placement="top">
                        <el-input type="text" v-model="PositionRequire.PositionSalary" autocomplete="off"></el-input>
                    </el-tooltip>
                </el-form-item>
                <el-form-item
                    label="工作地点"
                    :rules="[
                        { required: true, message: '工作地点不能为空'}
                    ]"
                >
                    <el-cascader
                    :options="AreaOptions"
                    collapse-tags
                    v-model="PositionRequire.PositionArea"
                    clearable></el-cascader>
                </el-form-item>
                <el-form-item
                    label="工作经验"
                    :rules="[
                        { required: true, message: '工作经验不能为空'}
                    ]"
                >
                    <el-select v-model="PositionRequire.Workyear" placeholder="请选择">
                        <el-option
                        v-for="item in WorkyearOptions"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item
                    label="学历"
                    :rules="[
                        { required: true, message: '学历不能为空'}
                    ]"
                >
                    <el-select v-model="PositionRequire.Education" placeholder="请选择">
                        <el-option
                        v-for="item in EducationOptions"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item
                    label="工作类型"
                    :rules="[
                        { required: true, message: '工作类型不能为空'}
                    ]"
                >
                    <el-radio v-model="PositionRequire.JobNature" label="1">全职</el-radio>
                    <el-radio v-model="PositionRequire.JobNature" label="0">兼职</el-radio>
                </el-form-item>
                <el-form-item
                    label="是否校招"
                    :rules="[
                        { required: true, message: '是否校招不能为空'}
                    ]"
                >
                    <el-radio v-model="PositionRequire.isSchoolJob" label="1">校招</el-radio>
                    <el-radio v-model="PositionRequire.isSchoolJob" label="0">非校招</el-radio>
                </el-form-item>
                <el-form-item
                    label="职位诱惑"
                    :rules="[
                        { required: true, message: '职位优势不能为空'}
                    ]"
                >
                    <el-tooltip class="item" effect="dark" content="多个标签之间用英文状态下“|”分隔" placement="top">
                        <el-input type="text" v-model="PositionRequire.positionAdvantage" placeholder="请输入内容"></el-input>
                    </el-tooltip>
                </el-form-item>
                <el-form-item
                    label="职位分类"
                    :rules="[
                        { required: true, message: '职位分类不能为空'}
                    ]"
                >
                    <el-cascader
                    :options="PositionOptions"
                    collapse-tags
                    v-model="PositionRequire.PositionType"
                    clearable></el-cascader>
                </el-form-item>
                <el-form-item
                    label="技术标签"
                    :rules="[
                        { required: true, message: '技术标签不能为空'}
                    ]"
                >
                    <el-tooltip class="item" effect="dark" content="多个标签之间用英文状态下“|”分隔" placement="top">
                        <el-input type="text" v-model="PositionRequire.skillLabels" placeholder="请输入内容"></el-input>
                    </el-tooltip>
                </el-form-item>
                <el-form-item
                    label="职位标签"
                    :rules="[
                        { required: true, message: '职位标签不能为空'}
                    ]"
                >   
                    <el-tooltip class="item" effect="dark" content="多个标签之间用英文状态下“|”分隔" placement="top">
                        <el-input  type="text" v-model="PositionRequire.positionLabels" placeholder="请输入内容"></el-input>
                    </el-tooltip>
                </el-form-item>
                <el-form-item
                    label="行业标签"
                    :rules="[
                        { required: true, message: '行业标签不能为空'}
                    ]"
                >   
                    <el-tooltip class="item" effect="dark" content="多个标签之间用英文状态下“|”分隔" placement="top">
                        <el-input type="text" v-model="PositionRequire.industryLabels" placeholder="请输入内容"></el-input>
                    </el-tooltip>
                </el-form-item>
                <el-form-item label="职位描述">
                    <mavon-editor 
                        :subfield=false
                        :ishljs = "true"
                        boxShadowStyle="0 2px 12px 0 rgba(255, 255, 255, 0)"
                        v-model="PositionRequire.positionIntro" 
                        ref=md @imgAdd="imgAdd"
                        :toolbars="toolbars"
                        @save="savePosition"
                        placeholder="点击全屏实时预览"
                        style="min-height:500px"
                        >
                    </mavon-editor>
                </el-form-item>
                <el-form-item
                    label="地铁(线名)"
                    :rules="[
                        { required: true, message: '地铁(线名)不能为空'}
                    ]"
                >
                    <el-input v-model="PositionRequire.subwayLine" placeholder="请输入内容"></el-input>
                </el-form-item>
                <el-form-item
                    label="地铁(站名)"
                    :rules="[
                        { required: true, message: '地铁(站名)不能为空'}
                    ]"
                >
                    <el-input v-model="PositionRequire.stationName" placeholder="请输入内容"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="savePosition">发布</el-button>
                    <el-button @click="resetForm('PositionRequireForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </div>
      </div>
  </div>
</template>

<script>
export default {
    data () {
        return {
            user_id: '',
            company_id: '',
            PositionRequire: {
                PositionName: '',
                PositionSalary: '',
                PositionArea: '',
                Workyear: '',
                Education: '',
                JobNature: '',
                isSchoolJob: '',
                positionAdvantage: '',
                PositionType: '',
                skillLabels: '',
                positionLabels: '',
                industryLabels: '',
                positionIntro: '',
                subwayLine: '',
                stationName: '',
            },
            toolbars: this.settings.toolbars,
            AreaOptions: [],
            PositionOptions: [],
            EducationOptions: [
                {'value': 0, 'label': '小学'},
                {'value': 1, 'label': '初中'},
                {'value': 2, 'label': '高中'},
                {'value': 3, 'label': '专科'},
                {'value': 4, 'label': '本科'},
                {'value': 5, 'label': '硕士'},
                {'value': 6, 'label': '博士'}
            ],
            WorkyearOptions: [
                {'value': '应届毕业生', 'label': '应届毕业生'},
                {'value': '不限', 'label': '经验不限'},
                {'value': '1年以下', 'label': '1年以下'},
                {'value': '1-3年', 'label': '1-3年'},
                {'value': '3-5年', 'label': '3-5年'},
                {'value': '5-10年', 'label': '5-10年'}
            ]
        }
    },
    created () {
        this.user_id = sessionStorage.user_id;
        this.company_id = sessionStorage.company_id;
        this.AreaOptions = this.settings.AreaOptions;
        this.PositionOptions = this.settings.PositionOptions;
    },
    methods: {
        // 绑定@imgAdd event
        imgAdd(pos, $file){
            // 第一步.将图片上传到服务器.
            var formdata = new FormData();
            formdata.append('image', $file);
            axios({
                url: 'http://api.offend.com:8000/avatar/',
                method: 'post',
                data: formdata,
                headers: { 'Content-Type': 'multipart/form-data' },
            }).then((url) => {
                // 第二步.将返回的url替换到文本原位置![...](./0) -> ![...](url)
                /**
                 * $vm 指为mavonEditor实例，可以通过如下两种方式获取
                 * 1. 通过引入对象获取: `import {mavonEditor} from ...` 等方式引入后，`$vm`为`mavonEditor`
                 * 2. 通过$refs获取: html声明ref : `<mavon-editor ref=md ></mavon-editor>，`$vm`为 `this.$refs.md`
                 */
                $vm.$img2Url(pos, url);
            })
        },
        savePosition() {
            // this.$refs.md.d_value
            // this.$refs.md.d_render
            this.axios.post(`${this.settings.Host}/home/position/add/`, {
                    publisher: this.user_id,
                    companyId: this.company_id,
                    positionName: this.PositionRequire.PositionName,
                    salary: this.PositionRequire.PositionSalary,
                    city: this.PositionRequire.PositionArea[0] + "-" + this.PositionRequire.PositionArea[1],
                    district: this.PositionRequire.PositionArea[2],
                    workYear: this.PositionRequire.Workyear,
                    education: this.PositionRequire.Education,
                    jobNature: this.PositionRequire.JobNature,
                    isSchoolJob: Number(this.PositionRequire.isSchoolJob),
                    positionAdvantage: this.PositionRequire.positionAdvantage,
                    firstType: this.PositionRequire.PositionType[0],
                    secondType: this.PositionRequire.PositionType[1],
                    thirdType: this.PositionRequire.PositionType[2],
                    skillLabels: this.PositionRequire.skillLabels,
                    positionLabels: this.PositionRequire.positionLabels,
                    industryLabels: this.PositionRequire.industryLabels,
                    positionIntro: this.PositionRequire.positionIntro,
                    positionIntroHtml: this.$refs.md.d_render,
                    subwayLine: this.PositionRequire.subwayLine,
                    stationName: this.PositionRequire.stationName,
                    orders: 1,
                    is_show: 1
            }).then(response => {
                // this.articleValue = "";
                // this.articleInfo.title = "";
                // this.articleInfo.tag = "";
                this.$notify({
                    title: '成功',
                    message: '职位发表成功',
                    type: 'success'
                });
                this.PositionRequire = {}
            }).catch(error => {
                this.$notify({
                    title: '失败',
                    message: '请检查是否有空白选项',
                    type: 'error'
                });
            })
        }
    }
}
</script>

<style lang="less" rel="stylesheet/less">
.create-position {
    background-color: #f6f6f6;
    .container {
        header {
            width: 840px;
            margin: 0 auto;
            padding: 20px 0;
            font-size: 32px;
            color: #333;
        }
        .form-wrapper {
            width: 840px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            margin-bottom: 20px;
            .el-input {
                width: 100%;
            }
            .el-cascader {
                width: 100%;
            }
            .el-select {
                width: 100%;

            }
        }
    }
}
</style>