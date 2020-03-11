<template>
  <div class="edit-resume">
    <div class="container">
        <header>编辑简历</header>
        <div class="editor">
            <div id="main">
                <div class="article-desc">
                    <el-form :label-position="labelPosition" label-width="80px" :model="resume">
                    <el-form-item label="简历标题">
                        <el-input v-model="resume.title"></el-input>
                    </el-form-item>
                    <el-form-item label="是否公开">
                        <el-radio v-model="resume.isShow" label="0">仅自己可见</el-radio>
                        <el-radio v-model="resume.isShow" label="1">公开</el-radio>
                    </el-form-item>
                    </el-form>
                </div>
                <mavon-editor 
                :subfield=false
                :ishljs = "true"
                boxShadowStyle="0 2px 12px 0 rgba(255, 255, 255, 0)"
                v-model="resume.md_code" 
                ref=md @imgAdd="imgAdd"
                :toolbars="toolbars"
                @save="updateResume"
                placeholder="点击全屏实时预览"
                style="min-height:500px"
                >
                </mavon-editor>
                <div class="operate">
                    <a href="javascript:;">点击 <i class="fa fa-save"></i> 保存</a>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    data () {
        return {
            resume_id: '',
            labelPosition: 'left',
            resume: {},
            toolbars: this.settings.toolbars
        }
    },
    created () {
        this.resume_id = this.$route.params.id;
        this.getResume(this.resume_id);
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
        // 获取简历信息
        getResume(resume_id) {
            this.axios.get(`${this.settings.Host}/resume/${resume_id}/`)
            .then(response => {
                this.resume = response.data;
            })
        },
        // 保存简历
        updateResume (markdown, html) {
            this.axios.post(`${this.settings.Host}/resume/${this.resume_id}/`, {
                title: this.resume.title,
                html_code: html,
                md_code: markdown,
                is_show: Number(this.resume.isShow),
                user: this.resume.user
            }).then(response => {
                this.$notify({
                title: '成功',
                message: '您的简历修改成功',
                type: 'success'
                });
            }).catch(error => {
                console.log(error)
                this.$notify({
                title: '失败',
                message: '请检查是否有空缺项',
                type: 'error'
                });
            })
        }
    }
}
</script>

<style lang="less" rel="stylesheet/less">
.edit-resume {
    background-color: #f6f6f6;
    .container {
        header {
            padding: 20px 0;
            font-size: 32px;
            color: #333;
        }
        .editor {
            background-color: #fff;
            border-radius: 10px;
            margin-bottom: 20px;
            #main {
            .article-desc {
                padding: 25px 25px 0 25px;
            }
            .operate {
                padding: 10px;
                display: flex;
                flex-wrap: nowrap;
                flex-direction: row-reverse;
                a {
                display: inline-block;
                color: #969696;
                padding: 5px 10px;
                }
            }
            }
        }
    }
}
</style>