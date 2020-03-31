<template>
  <div class="change">
      <div class="container">
        <div class="content" v-if="user_type == 1">
          <embed class="bg" src="../../../static/imgs/undraw_updated_resume_u4fy.svg">
          <p class="operate"><a href="javascript:;" @click="changeUsertype"><i class="el-icon-right"></i> 求职者</a></p>
        </div>

        <div class="content" v-if="user_type == 0">
          <embed class="bg" src="./../../static/imgs/undraw_special_event_4aj8.svg">
          <p class="operate"><a href="javascript:;" @click="changeUserTypeDialog=true"><i class="el-icon-right"></i> 招人</a></p>
        </div>
      </div>
      <el-dialog title="企业用户认证" :visible.sync="changeUserTypeDialog">
        <el-form :model="form">
          <el-form-item label="公司名称" :label-width="formLabelWidth">
            <el-autocomplete
              class="inline-input"
              v-model="form.companyName"
              :fetch-suggestions="querySearch"
              placeholder="请输入公司名称"
              :trigger-on-focus="false"
              @select="handleSelect"
            ></el-autocomplete>
          </el-form-item>
          <el-form-item label="企业邮箱" :label-width="formLabelWidth">
            <el-input type="email" v-model="form.email" autocomplete="off" placeholder="请输您在该公司的邮箱"></el-input>
          </el-form-item>
          <el-form-item label="手机号" :label-width="formLabelWidth">
            <el-input type="text" maxlength="11" v-model="form.mobile" autocomplete="off" placeholder="请确认您的手机号"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="changeUserTypeDialog = false">取 消</el-button>
          <el-button type="primary" @click="companyAuth">确 定</el-button>
        </div>
      </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user_type: '',
      changeUserTypeDialog: false,
      formLabelWidth: '120px',
      form: {
        companyName: '',
        email: '',
        mobile: ''
      },
    }
  },
  created () {
    this.user_type = sessionStorage.user_type;
  },
  methods: {
    changeUsertype () {
      Swal.fire({
        title: '确定修改为求职者吗?',
        text: "该操作将解除与当前公司的关系，清除发布的职位",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: '取消',
        confirmButtonText: '确定'
      }).then((result) => {
        if (result.value) {
          Swal.mixin({
            input: 'text',
            // confirmButtonText: 'Next &rarr;',
            confirmButtonText: '确定',
            showCancelButton: true,
            // progressSteps: ['1']
          }).queue([
            {
              // title: 'Question 1',
              text: '请确认手机号'
            }
          ]).then((result) => {
            if (result.value[0] != "") {
              this.axios
              .post(`${this.settings.Host}/change_user_type/`, {
                user_id: sessionStorage.user_id,
                mobile: result.value[0]
              }).then(res => {
                if (res.data.status == 200) {
                  Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: '您已经切换为求职者',
                    showConfirmButton: false,
                    timer: 1500
                  })
                  setTimeout(() => {
                    sessionStorage.clear();
                    location.href = "/"
                  }, 2000);
                } else {
                  Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: '身份切换失败，请重试',
                    showConfirmButton: false,
                    timer: 1500
                  })
                }
              }).catch(err => {
                Swal.fire({
                  position: 'center',
                  icon: 'error',
                  title: '请求失败，请重试',
                  showConfirmButton: false,
                  timer: 1500
                })
              })
            } else {
              Swal.fire({
                position: 'center',
                icon: 'error',
                title: '您的密码为空',
                showConfirmButton: false,
                timer: 1500
              })
            }
          })
        }
      })
    },
    handleSelect(item) {
      // console.log(item);
    },
    querySearch(queryString, cb) {
      this.axios.get(`${this.settings.Host}/home/search/companyname/`, {
        params: {
          queryString: queryString
        }
      }).then(res => {
        cb(res.data.data);
      }).catch(err => {
        console.log(err)
      })
    },
    companyAuth () {
      if (this.form.companyName == "" || this.form.email == "" || this.form.mobile == "") {
        this.$notify.error({
          title: '错误',
          message: '请填写公司名称和邮箱'
        });
      }
      this.axios.get(`${this.settings.Host}/user_auth/`, {
        params: {
          name: this.form.companyName,
          email: this.form.email,
          mobile: this.form.mobile,
          uid: sessionStorage.user_id
        }
      }).then(res => {
        if (res.data.status == 200) {
          this.changeUserTypeDialog = false
          this.$notify.success({
            title: '身份已切换',
            message: '3秒之后请重新登录'
          });
          setTimeout(() => {
            sessionStorage.clear();
            location.href = "/"
          }, 3000);
        } else {
          this.$notify.error({
            title: '错误',
            message: '请求错误，请重试'
          });
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style lang="less" rel="stylesheet/less">
.change {
  padding: 50px 0;
  background-color: #f6f6f6;
  .container {
    .content {
      position: relative;
      .bg {
        margin: 0 auto;
        display: block;
        width: 700px;
      }
      .operate {
        position: absolute;
        display: block;
        top: 50%;
        left: 50%;
        margin-left: -75px;
        margin-top: -25px;
        font-size: 25px;
        height: 50px;
        width: 150px;
        text-align: center;
        line-height: 50px;
        background: #6c63ff;
        transition: all .3s;
        a {
          color: #fff;
        }
        &:hover {
          transform: scale(1.25);
          box-shadow: 0 0 0.7rem 0.1875rem rgba(0, 0, 0, 0.2);
        }
      }
    }
  }
  .el-autocomplete {
    .el-input {
      width: 500px;
    }
  }
}
</style>