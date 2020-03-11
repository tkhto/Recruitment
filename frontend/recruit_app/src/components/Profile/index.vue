<template>
  <div class="profile">
    <div class="top-banner" v-bind:style="{ backgroundImage: 'url('+ bannerImg +')'}">
    </div>
    <div class="info-first">
      <div class="container">
          <div class="left">
            <span class="img-wrapper" v-bind:style="{ backgroundImage: 'url('+userInfo.avatar +')'}">
            </span>
          </div>
          <div class="right">
            <p class="name">{{ userInfo.nic_name }} <span class="edit-profile" @click="dialogFormVisible = true"><i class="el-icon-edit"></i> 修改资料</span></p>
            <p class="intro">{{ userInfo.intro }}</p>
            <p class="social">
              <a v-if="userInfo.site" :href="userInfo.site" target="_blank"><i class="fa fa-home"></i></a>
              <a v-if="userInfo.facebook" :href="userInfo.facebook" target="_blank"><i class="fa fa-facebook"></i></a>
              <a v-if="userInfo.twitter" :href="userInfo.twitter" target="_blank"><i class="fa fa-twitter"></i></a>
              <a v-if="userInfo.weibo" :href="userInfo.weibo" target="_blank"><i class="fa fa-weibo"></i></a>
              <a v-if="userInfo.email" :href="'mailto:'+userInfo.email" target="_blank"><i class="fa fa-envelope-o"></i></a>
              <a v-if="userInfo.github" :href="userInfo.github" target="_blank"><i class="fa fa-github"></i></a>
            </p>
          </div>
      </div>
    </div>
    <div class="info-second">
      <div class="container">
          <el-row :gutter="20">
            <el-col :span="5">
              <div class="grid-content">
                <div class="info-saide">
                  <p class="follow">
                    <span><router-link tag="b" to="/">99</router-link><i>已关注</i></span>
                    <span><router-link tag="b" to="/">99M</router-link><i>粉丝</i></span>
                  </p>
                  <ul>
                    <li><a :class="{'active': panel_id=='news'}" href="javascript:;" @click="panel_id='news';filters.page=1"><i class="el-icon-files"></i> 动态</a></li>
                    <li><a :class="{'active': panel_id=='article'}" href="javascript:;" @click="panel_id='article';filters.page=1"><i class="el-icon-document"></i> 文章</a></li>
                    <li><a :class="{'active': panel_id=='resume'}" href="javascript:;" @click="panel_id='resume';filters.page=1"><i class="el-icon-document-checked"></i> 简历</a></li>
                    <li><a :class="{'active': panel_id=='collect'}" href="javascript:;" @click="panel_id='collect';filters.page=1"><i class="el-icon-star-off"></i> 收藏</a></li>
                  </ul>
                </div>
              </div>
            </el-col>
            <el-col :span="14">
              <div class="grid-content">
                <div class="info-content" v-if="panel_id == 'news'">
                  <div class="editor">
                    <div id="main">
                        <mavon-editor 
                        :subfield=false
                        :ishljs = "true"
                        boxShadowStyle="0 2px 12px 0 rgba(255, 255, 255, 0)"
                        v-model="newsValue" 
                        ref=md @imgAdd="imgAdd"
                        :toolbars="toolbars"
                        @save="saveNews"
                        placeholder="发个动态，见证当下～"
                        style="min-height:150px"
                        >
                        </mavon-editor>
                        <div class="operate">
                          <a href="javascript:;">点击 <i class="fa fa-save"></i> 发表</a>
                        </div>
                    </div>
                  </div>
                  <News @removeItem="refresh_list()" v-for="(item, i) in news_list.results" :key="i" v-bind:item="item" v-bind:userInfo="userInfo"></News>
                  <el-pagination
                    background
                    @current-change="handleCurrentChange"
                    layout="prev, pager, next"
                    :total="news_list.count">
                  </el-pagination>
                </div>
                <div class="info-content" v-if="panel_id == 'article'">
                  <a class="create" :href="`/createarticle/${this.user_id}`" target="_blank"><i class="el-icon-circle-plus-outline"></i> 创建新文章</a>
                  <Articles @removeItem="refresh_list()" v-for="(item, i) in article_list.results" :key="i" v-bind:item="item" v-bind:userInfo="userInfo"></Articles>
                  <el-pagination
                    background
                    @current-change="handleCurrentChange"
                    layout="prev, pager, next"
                    :total="article_list.count">
                  </el-pagination>
                </div>
                <div class="info-content" v-if="panel_id == 'collect'">
                  <Collections v-for="(item, i) in collect_list" :key="i" v-bind:item="item" v-bind:userInfo="userInfo"></Collections>
                  <el-pagination
                    background
                    @current-change="handleCurrentChange"
                    layout="prev, pager, next"
                    :total=news_list.count>
                  </el-pagination>
                </div>
                <div class="info-content" v-if="panel_id == 'resume'">
                  <a class="create" :href="`/createresume/${this.user_id}`" target="_blank"><i class="el-icon-circle-plus-outline"></i> 创建简历</a>
                  <div class="resume-wrapper">
                    <Resume @removeItem="refresh_list()" v-for="(item, i) in resume_list.results" :key="i" v-bind:item="item" v-bind:userInfo="userInfo"></Resume>
                  </div>
                  <el-pagination
                    background
                    :pageSize="6"
                    @current-change="handleCurrentChange"
                    layout="prev, pager, next"
                    :total="resume_list.count">
                  </el-pagination>
                </div>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="grid-content">
                <div class="comment-saide">
                  <p class="comment-title">最近评论</p>
                  <ul class="comment-wrapper">
                    <li class="comment-item">
                      <div class="pub-time">
                        <span>2020</span>
                        <span class="month">Mar</span>
                        <span>23</span>
                      </div>
                      <p class="comment">阿达胡说八道讲哈不是大家哈是的哈是多久啊</p>
                    </li>
                    <li class="comment-item">
                      <div class="pub-time">
                        <span>2020</span>
                        <span class="month">Mar</span>
                        <span>23</span>
                      </div>
                      <p class="comment">阿达胡说八道讲哈不是大家哈是的哈是多久啊</p>
                    </li>
                    <li class="comment-item">
                      <div class="pub-time">
                        <span>2020</span>
                        <span class="month">Mar</span>
                        <span>23</span>
                      </div>
                      <p class="comment">阿达胡说八道讲哈不是大家哈是的哈是多久啊</p>
                    </li>
                  </ul>
                </div>
              </div>
            </el-col>
          </el-row>
      </div>
    </div>
    <el-dialog title="编辑个人资料" :visible.sync="dialogFormVisible">
      <el-tabs v-model="activeName">
        <el-tab-pane label="基本信息" name="first">
          <el-form :model="userInfo">
            <el-form-item label="头像" :label-width="formLabelWidth">
              <el-upload
                class="avatar-uploader"
                action="http://api.offend.com:8000/avatar/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload">
                <img v-if="userInfo.avatar" :src="'http://api.offend.com:8000/media/' + userInfo.avatar" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </el-form-item>
            <el-form-item label="昵称" :label-width="formLabelWidth">
              <el-input v-model="userInfo.nic_name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="性别" :label-width="formLabelWidth">
              <el-radio v-model="userInfo.gender" label="1">男</el-radio>
              <el-radio v-model="userInfo.gender" label="0">女</el-radio>
            </el-form-item>
            <el-form-item label="生日" :label-width="formLabelWidth">
              <el-date-picker
                v-model="userInfo.birthday"
                type="date"
                placeholder="选择日期"
                value-format="yyyy-MM-dd">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="介绍" :label-width="formLabelWidth">
              <el-input type="textarea" v-model="userInfo.intro"></el-input>
            </el-form-item>
            <el-form-item label="角色" :label-width="formLabelWidth">
              <el-radio v-model="userInfo.user_type" label="0">求职者</el-radio>
              <el-radio v-model="userInfo.user_type" label="1">招人者</el-radio>
            </el-form-item>
            <el-form-item label="所在城市" :label-width="formLabelWidth">
              <el-input v-model="userInfo.city" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="任职公司" :label-width="formLabelWidth">
              <el-input v-model="userInfo.companyId" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="岗位" :label-width="formLabelWidth">
              <el-input v-model="userInfo.selfPosition" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="工作状态" :label-width="formLabelWidth">
              <el-radio v-model="userInfo.work_status" label="0">已离职</el-radio>
              <el-radio v-model="userInfo.work_status" label="1">在职</el-radio>
              <el-radio v-model="userInfo.work_status" label="2">保密</el-radio>
              <el-radio v-model="userInfo.work_status" label="3">已退休</el-radio>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="社交信息" name="second">
          <el-form :model="userInfo">
            <el-form-item label="手机" :label-width="formLabelWidth">
              <el-input v-model="userInfo.mobile" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="邮箱" :label-width="formLabelWidth">
              <el-input v-model="userInfo.email" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="博客" :label-width="formLabelWidth">
              <el-input v-model="userInfo.site" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="微博" :label-width="formLabelWidth">
              <el-input v-model="userInfo.weibo" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="GitHub" :label-width="formLabelWidth">
              <el-input v-model="userInfo.github" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="FaceBook" :label-width="formLabelWidth">
              <el-input v-model="userInfo.facebook" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="twitter" :label-width="formLabelWidth">
              <el-input v-model="userInfo.twitter" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="教育信息" name="third">
          <el-form :model="userInfo">
            <el-form-item label="毕业院校" :label-width="formLabelWidth">
              <el-input v-model="userInfo.graduatedSchool" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="学历" :label-width="formLabelWidth">
              <el-select v-model="userInfo.education" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="专业" :label-width="formLabelWidth">
              <el-input v-model="userInfo.specialty" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="是否统招" :label-width="formLabelWidth">
              <el-radio v-model="userInfo.unifiedAdmission" label="1">统招</el-radio>
              <el-radio v-model="userInfo.unifiedAdmission" label="0">非统招</el-radio>
            </el-form-item>
            <el-form-item label="在校时间" :label-width="formLabelWidth">
              <el-date-picker
                v-model="userInfo.admissionTime"
                type="date"
                placeholder="选择日期"
                value-format="yyyy-MM-dd">
              </el-date-picker>
              至
              <el-date-picker
                v-model="userInfo.graduationTime"
                type="date"
                placeholder="选择日期"
                value-format="yyyy-MM-dd">
              </el-date-picker>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false;submitProfile()">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import News from "./News/index"
import Collections from "./Collections/index"
import Articles from "./Articles/index"
import Resume from "./Resume/index"
import CKEditor from "../Common/CKEditor5"

export default {
  data() {
    return {
      activeName: 'first',
      user_id: '',
      bannerImg: "../../../static/imgs/banner.jpg",
      imageUrl: '',
      options: [
        {value: 0, label: '小学'},
        {value: 1, label: '初中'},
        {value: 2, label: '高中'},
        {value: 3, label: '专科'},
        {value: 4, label: '本科'},
        {value: 5, label: '硕士'},
        {value: 6, label: '博士'}],
      userInfo: {},
      panel_id: 'news',  // 当前所在子页面
      news_list: [],
      article_list: [],
      collect_list: [],
      resume_list: [],
      dialogFormVisible: false,  // 个人资料表单模态框
      formLabelWidth: '120px',  // 表单label的宽度
      newsValue: '', // 动态的值
      toolbars: this.settings.toolbars,  // 编辑器工具栏配置
      filters: { // 分页条件
        page: 1
      }
    };
  },
  created () {
    this.user_id = sessionStorage.user_id;
    this.get_profile();
    this.getData();
  },
  watch: {
    'panel_id' () {
      this.getData();
    },
    "filters.page" () {
      this.getData();
    }
  },
  methods: {
    submitProfile () {
      const params = {
        "nic_name": this.userInfo.nic_name,
        "avatar": this.userInfo.avatar,
        "gender": this.userInfo.gender,
        "birthday": this.userInfo.birthday,
        "intro": this.userInfo.intro,
        "user_type": this.userInfo.user_type,
        "city": this.userInfo.city,
        "companyId": this.userInfo.companyId,
        "selfPosition": this.userInfo.selfPosition,
        "work_status": this.userInfo.work_status,
        "mobile": this.userInfo.mobile,
        "email": this.userInfo.email,
        "site": this.userInfo.site,
        "weibo": this.userInfo.weibo,
        "github": this.userInfo.github,
        "facebook": this.userInfo.facebook,
        "twitter": this.userInfo.twitter,
        "graduatedSchool": this.userInfo.graduatedSchool,
        "education": this.userInfo.education,
        "specialty": this.userInfo.specialty,
        "unifiedAdmission": this.userInfo.unifiedAdmission,
        "schoolTime": this.userInfo.schoolTime,
        "admissionTime": this.userInfo.admissionTime,
        "graduationTime": this.userInfo.graduationTime,
      }
      const config = {
          headers: {
              "Content-Type": "multipart/form-data;charset=utf-8"
          }
      }
      this.axios.post(`${this.settings.Host}/profile/${this.user_id}/`,params).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error)
      })
    },
    // 获取个人信息
    async get_profile () {
      const response = await this.axios.get(`${this.settings.Host}/profile/${this.user_id}/`)
      this.userInfo = response.data
    },
    // 上传头像成功后的操作
    handleAvatarSuccess(res, file) {
      this.userInfo.avatar = res.url;
      // this.userInfo.avatar = URL.createObjectURL(file.raw);
    },
    // 上传之前进行校验
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    },
    // 获取动态，文章，收藏，简历
    async getData () {
      const response = await this.axios.get(`${this.settings.Host}/${this.panel_id}/?${this.panel_id}=${this.user_id}`, {
        params: this.filters
      });
      if (this.panel_id == 'news') {
        this.news_list = response.data;
      } else if (this.panel_id == 'article') {
        this.article_list = response.data;
      } else if (this.panel_id == 'collect') {
        this.collect_list = response.data;
      } else if (this.panel_id == 'resume') {
        this.resume_list = response.data;
      }
    },
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
    // 保存动态
    saveNews(markdown, html) {
      // 此时会自动将 markdown 和 html 传递到这个方法中
      this.axios.post(`${this.settings.Host}/news/`, {
          user: this.user_id,
          content: html
      }).then(response => {
        this.getData();
        this.newsValue = "";
        this.$notify({
          title: '成功',
          message: '动态发表成功',
          type: 'success'
        });
      }).catch(error => {
        this.$notify({
          title: '失败',
          message: '动态内容不能为空',
          type: 'error'
        });
      })
    },
    // 刷新当前列表
    refresh_list () {
      this.getData();
    },
    // 处理分页
    handleCurrentChange (page) {
      this.filters.page = page;
    }
  },
  components: {
    News, Collections, Articles, Resume, CKEditor
  }
};
</script>

<style lang="less" rel="stylesheet/less">
.profile {
  .top-banner {
    height: 200/16rem;
    background-size: cover;
  }
  .info-first {
    position: relative;
    height: 120/16rem;
    .container {
      .left {
        position: absolute;
        width: 200/16rem;
        height: 200/16rem;
        margin-right: 30/16rem;
        top: -100/16rem;
        float: left;
        .img-wrapper {
          display: inline-block;
          width: inherit;
          height: inherit;
          background-size: cover;
          border: 5/16rem solid #fff;
          box-sizing: border-box;
          border-radius: 50%;
          box-shadow: 0 0 20/16rem 0 #929292;
        }
      }
      .right {
        display: flex;
        padding-left: 20px;
        justify-content: center;
        flex-direction: column;
        height: 120/16rem;
        margin-left: 230px;
        .name {
          margin-bottom: 5px;
          font-size: 30px;
          font-weight: 500;
          color: #333;
          .edit-profile {
            display: inline-block;
            height: 35px;
            padding: 0 10px;
            margin: 5px 0;
            float: right;
            box-sizing: border-box;
            border: 2px solid #eee;
            line-height: 31px;
            border-radius: 22px;
            font-size: 14px;
            color: #666;
            transition: all .3s;
            cursor: pointer;
            &:hover {
              color: #333;
              border: 2px solid #999;
            }
          }
        }
        .intro {
          margin-bottom: 5px;
          font-size: 16px;
          color: #333;
        }
        .social {
          color: #717171;
          font-size: 14px;
          a {
            display: inline-block;
            width: 30px;
            margin-right: 10px;
            padding: 2px 5px;
            border-radius: 5px;
            text-align: center;
            color: #666;
            cursor: pointer;
            &:hover {
              color: #333;
              background-color: #eee;
            }
          }
        }
      }
    }
  }
  .info-second {
    background: #f6f6f6;
    .container {
        .el-row {
          margin-bottom: 20px;
          &:last-child {
            margin-bottom: 0;
          }
          .el-col {
            border-radius: 4px;
            .grid-content {
              border-radius: 4px;
              min-height: 36px;
              .info-saide {
                padding: 20/16rem 0;
                p {
                  margin-bottom: 20/16rem;
                  color: #333;
                }
                .follow {
                  display: flex;
                  padding: 10px 0;
                  justify-content: space-around;
                  flex-wrap: nowrap;
                  border-radius: 10px;
                  background-color: #fff;
                  span {
                    display: block;
                    i {
                      display: block;
                      text-align: center;
                      color: #555;
                    }
                    b {
                      display: block;
                      text-align: center;
                      font-size: 30px;
                      font-weight: 500;
                    }
                  }
                }
                ul {
                  padding: 10px 20px;
                  background-color: #fff;
                  border-radius: 10px;
                  li {
                    height: 40px;
                    line-height: 40px;
                    text-align: center;
                    a {
                      color: #333;
                      i {
                        margin-right: 20px;
                      }
                    }
                    .active {
                      color: #0094ff;
                    }
                  }
                }
              }
              .info-content {
                margin: 20px 0;
                .create {
                  display: block;
                  padding: 20px 0;
                  margin-bottom: 20px;
                  padding-left: 20px;
                  font-size: 32px;
                  color: #333;
                  background-color: #fff;
                  border-radius: 10px;
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
                .resume-wrapper {
                  display: flex;
                  flex-wrap: wrap;
                  justify-content: space-between;
                }
                .el-pagination {
                  padding: 20/16rem;
                  margin-bottom: 20/16rem;
                  text-align: center;
                }
              }
              .comment-saide {
                padding: 1.25rem 0;
                .comment-title {
                  font-size: 16px;
                  font-weight: 500;
                  color: #212121;
                  margin-bottom: 15px;
                }
                .comment-wrapper {
                  .comment-item {
                    display: flex;
                    justify-content: space-around;
                    flex-wrap: nowrap;
                    margin-bottom: 10px;
                    padding-bottom: 10px;
                    .pub-time {
                      width: 40/16rem;
                      display: flex;
                      justify-content: center;
                      flex-direction: column;
                      background-color: #349dff47;
                      border-radius: 3px;
                      span {
                        display: inline-block;
                        width: 40/16rem;
                        font-size: 12px;
                        text-align: center;
                        color: #004c9a;
                      }
                      .month {
                        background-color: #91c3f7;
                      }
                    }
                    .comment {
                      padding: 0 5px;
                      font-size: 14px;
                      color: #333;
                      line-height: 24px;
                      font-weight: 500;
                      background-color: #f6f6f6;
                    }
                  }
                  & > :not(:last-child) {
                    border-bottom: 1px dashed #7ebcfc;
                  }
                }
              }
            }
          }
        
      }
    }
  }
  .el-dialog__wrapper {
    .el-dialog {
      .el-dialog__body {
        .el-tabs__content {
          .el-tab-pane {
            .el-form {
              .avatar-uploader .el-upload {
                border: 1px dashed #d9d9d9;
                border-radius: 6px;
                cursor: pointer;
                position: relative;
                overflow: hidden;
              }
              .avatar-uploader .el-upload:hover {
                border-color: #409EFF;
              }
              .avatar-uploader-icon {
                font-size: 28px;
                color: #8c939d;
                width: 178px;
                height: 178px;
                line-height: 178px;
                text-align: center;
              }
              .avatar {
                width: 178px;
                height: 178px;
                display: block;
              }
            }
          }
        }
      }
    }
  }
}
.edit-article-dislog {
  .el-dialog__body {
    padding: 0px !important;
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