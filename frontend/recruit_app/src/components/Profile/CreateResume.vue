<template>
  <div class="create-resume">
    <div class="container">
        <header>创建简历</header>
        <div class="editor">
            <div id="main">
                <div class="article-desc">
                    <el-form :label-position="labelPosition" label-width="80px" :model="resumeInfo">
                    <el-form-item label="简历标题">
                        <el-input v-model="resumeInfo.title"></el-input>
                    </el-form-item>
                    <el-form-item label="是否公开">
                        <el-radio v-model="resumeInfo.is_show" label="0">仅自己可见</el-radio>
                        <el-radio v-model="resumeInfo.is_show" label="1">公开</el-radio>
                    </el-form-item>
                    </el-form>
                </div>
                <mavon-editor 
                :subfield=false
                :ishljs = "true"
                boxShadowStyle="0 2px 12px 0 rgba(255, 255, 255, 0)"
                v-model="resumeValue" 
                ref=md @imgAdd="imgAdd"
                :toolbars="toolbars"
                placeholder="点击全屏实时预览"
                style="min-height:500px"
                >
                </mavon-editor>
                <div class="operate">
                    <a href="javascript:;" @click="saveResume">保存</a>
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
            user_id: '',
            labelPosition: 'left',
            resumeInfo: {
                title: '',
                is_show: 0
            },
            resumeValue: '',
            toolbars: this.settings.toolbars
        }
    },
    created () {
        this.user_id = sessionStorage.user_id;
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
        // 保存简历
        saveResume () {
            this.axios.post(`${this.settings.Host}/resume/`, {
                title: this.resumeInfo.title,
                html_code: this.$refs.md.d_render,
                md_code: this.$refs.md.d_value,
                is_show: Number(this.resumeInfo.is_show),
                user: this.user_id
            }).then(response => {
                this.$notify({
                    title: '成功',
                    message: '您创建了一份新的简历',
                    type: 'success'
                });
                this.resumeValue = "";
                this.resumeInfo.title = "";
            }).catch(error => {
                this.$notify({
                    title: '失败',
                    message: '只能创建一份简历，或字段有空缺项',
                    type: 'error'
                });
            })
        }
    }
}
</script>

<style lang="less" rel="stylesheet/less">
.create-resume {
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
                    color: #ffffff;
                    padding: 5px 10px;
                    background-color: #2fa4fe;
                    border-radius: 5px;
                }
            }
            }
        }
    }
}
</style>