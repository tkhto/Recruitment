<template>
  <div class="edit-article">
    <div class="container">
      <header>编辑文章</header>
      <div class="editor">
        <div id="main">
          <div class="article-desc">
            <el-form :label-position="labelPosition" label-width="80px" :model="article">
              <el-form-item label="标题">
                <el-input v-model="article.title"></el-input>
              </el-form-item>
              <el-form-item label="标签">
                <el-popover
                  placement="top-start"
                  width="200"
                  trigger="hover"
                  content="多个标签之间用英文状态下“|”分隔"
                >
                  <el-input slot="reference" v-model="article.tag"></el-input>
                </el-popover>
              </el-form-item>
            </el-form>
          </div>
          <mavon-editor
            :subfield="false"
            :ishljs="true"
            boxShadowStyle="0 2px 12px 0 rgba(255, 255, 255, 0)"
            v-model="article.md_code"
            ref="md"
            @imgAdd="imgAdd"
            :toolbars="toolbars"
            @save="editArticle"
            placeholder="点击全屏实时预览"
            style="min-height:150px"
          ></mavon-editor>
          <div class="operate">
            <a href="javascript:;" @click="editArticle">
              更新
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            user_id: '',
            article_id: "",
            labelPosition: "left",
            article: {},
            toolbars: this.settings.toolbars
        };
    },
    created() {
        this.article_id = this.$route.params.id;
        this.user_id = sessionStorage.user_id;
        this.articleRetrieve(this.article_id);
    },
    methods: {
        // 绑定@imgAdd event
        imgAdd(pos, $file) {
        // 第一步.将图片上传到服务器.
        var formdata = new FormData();
        formdata.append("image", $file);
        axios({
            url: "http://api.offend.com:8000/avatar/",
            method: "post",
            data: formdata,
            headers: { "Content-Type": "multipart/form-data" }
        }).then(url => {
            // 第二步.将返回的url替换到文本原位置![...](./0) -> ![...](url)
            /**
             * $vm 指为mavonEditor实例，可以通过如下两种方式获取
             * 1. 通过引入对象获取: `import {mavonEditor} from ...` 等方式引入后，`$vm`为`mavonEditor`
             * 2. 通过$refs获取: html声明ref : `<mavon-editor ref=md ></mavon-editor>，`$vm`为 `this.$refs.md`
             */
            $vm.$img2Url(pos, url);
        });
    },
    // 获取单篇文章信息
    articleRetrieve(article_id) {
        this.axios.get(`${this.settings.Host}/article/${article_id}/`)
        .then(response => {
          this.article = response.data.result;
        });
    },
    // 更新文章
    editArticle() {
      this.axios
        .post(`${this.settings.Host}/article/${this.article.id}/`, {
          user: this.user_id,
          title: this.article.title,
          tag: this.article.tag,
          html_code: this.$refs.md.d_render,
          md_code: this.$refs.md.d_value
        })
        .then(response => {
          this.$notify({
            title: "成功",
            message: "文章修改成功",
            type: "success"
          });
        })
        .catch(error => {
          this.$notify({
            title: "失败",
            message: "文章修改失败",
            type: "error"
          });
        });
    }
  }
};
</script>

<style lang="less" rel="stylesheet/less">
.edit-article {
  background-color: #f6f6f6;
  .container {
    header {
      padding: 20px 0;
      width: 840px;
      margin: 0 auto;
      font-size: 32px;
      color: #333;
    }
    .editor {
      width: 840px;
      margin: 0 auto 20px;
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