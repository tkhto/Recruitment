<template>
  <div class="index">
    <div class="topbar">
        <div class="container">
            <div class="top-left">
                <a class="logo" href="javascript:;">Offend</a>
                <div class="curr-addr">
                    <span>{{ curr_province }}</span>
                    <a href="javascript:;" @click="changeAddrDialog = true"><i class="el-icon-location"></i> 切换城市</a>
                </div>
                <ul class="top-tabs">
                    <li class="tab-item"><a href="javascript:;">公司</a></li>
                    <li class="tab-item"><a href="javascript:;">校园招聘</a></li>
                    <li class="tab-item"><a href="javascript:;">社区</a></li>
                </ul>
            </div>
            <ul class="top-right">
                <li class="top-item"><a href="javascript:;"><i class="el-icon-upload"></i> 上传简历</a></li>
                <li class="top-item"><a href="javascript:;" @click="loginPanel = true"><i class="el-icon-s-custom"></i> 登录</a></li>
                <li class="top-item"><a href="javascript:;" @click="loginPanel = true">注册</a></li>
            </ul>
        </div>
    </div>
    <!-- 登录注册 弹出框 -->
    <el-dialog :visible.sync="loginPanel" width="30%" center>
      <h1 class="dialog-logo">Offend</h1>
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="登录" name="first">
          <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm" class="demo-ruleForm">
              <el-form-item prop="account">
                <el-input type="text" v-model="loginForm.account" autocomplete="off" placeholder="手机号" suffix-icon="el-icon-mobile-phone"></el-input>
              </el-form-item>
              <el-form-item prop="checkPass">
                <el-input type="password" v-model="loginForm.checkPass" autocomplete="off" placeholder="密码" suffix-icon="el-icon-key"></el-input>
              </el-form-item>
              <div id="geetest1"></div>
              <el-form-item>
                <el-button class="account-btn" @click="submitLoginForm('loginForm')">登录</el-button>
              </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="注册" name="second">
          <el-form :model="registForm" status-icon :rules="rules" ref="registForm" class="demo-ruleForm">
              <el-form-item prop="mobile">
                <el-input type="text" v-model="registForm.mobile" autocomplete="off" placeholder="手机号" suffix-icon="el-icon-mobile-phone"></el-input>
              </el-form-item>
              <el-form-item prop="rpassword">
                <el-input type="password" v-model="registForm.rpassword" autocomplete="off" placeholder="密码" suffix-icon="el-icon-mobile-phone"></el-input>
              </el-form-item>
              <el-form-item prop="sms">
                <el-input type="text" v-model="registForm.sms" autocomplete="off" placeholder="验证码" suffix-icon="el-icon-key">
                  <template slot="append">
                    <el-button type="primary" size="middle" @click="get_code">获取验证码</el-button>
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-button  class="account-btn" @click="submitRegistForm('registForm')">注册</el-button>
              </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-dialog>
    <!-- 换站 弹出框 -->
    <el-dialog class="city-list" title="切换城市" :visible.sync="changeAddrDialog" width="45%">
      <div class="tips">
        <h1 class="tips-head">亲爱的用户您好:</h1>
        <p class="tips-desc">切换城市分站，让我们为您提供更准确的职位信息。</p>
      </div>
      <el-divider></el-divider>
      <el-button v-for="item in provinceList" :key="item.id" class="button" @click="changeProvince(item.name)">{{ item.name }}</el-button>
    </el-dialog>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    // 验证手机号
    let validateAccount = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入手机号'));
      } else if (!this.check_mobile(value)) {
          callback(new Error("手机号格式错误"));
      }
      callback();
    };
    // 验证密码
    let validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else if (value.length < 6 || value.length > 16) {
        callback(new Error('密码长度为6～16位'));
      }
      callback();
    };
    // 验证验证码
    let validateSms = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入验证码'));
      }
      callback();
    };
    return {
      provinceList: [],
      curr_province: '北京市',
      activeName: 'first',
      changeAddrDialog: false,
      loginPanel: false,
      searchCon: "",
      loginForm: {
        account: '',
        checkPass: ''
      },
      registForm: {
        mobile: '',
        rpassword: '',
        sms: ''
      },
      rules: {
        account: [
          { validator: validateAccount, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        mobile: [
          { validator: validateAccount, trigger: 'blur' }
        ],
        rpassword: [
          { validator: validatePass, trigger: 'blur' }
        ],
        sms: [
          { validator: validateSms, trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.getProvince()
  },
  methods: {
    check_mobile (mobile) {
      const reg = /^1[3-9]\d{9}$/
      if (!reg.test(mobile)) {
          return false;
      }
      return true
    },
    async getProvince () {
      const response = await this.axios.get(`${this.settings.Host}/province/`)
      this.provinceList = response.data
    },
    changeProvince (province) {
      this.curr_province = province;
      this.changeAddrDialog = false;
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },
    // 登录处理
    submitLoginForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.get_geetest_capcha()
        } else {
          this.$message.error("对不起，信息不正确");
          return false;
        }
      });
    },
    // 注册处理
    submitRegistForm(formName) {
      // 验证数据
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 提交数据
          this.axios.post(`${this.settings.Host}/`,{
              mobile: this.registForm.mobile,
              password: this.registForm.rpassword,
              sms_code: this.registForm.sms,
          }).then(response=>{
              // 注册成功!保存登录状态
              sessionStorage.user_id = response.data.id;
              sessionStorage.user_name = response.data.username;
              sessionStorage.user_token = response.data.token;
              let self = this;
              this.$message.success("注册成功！");
              this.loginPanel = false;
              this.$refs.registForm.resetFields();
          }).catch(error => {
            console.log(error)
              this.$message.error("注册用户失败！");
          })
        } else {
          this.$message.error("对不起，账号密码错误");
          return false;
        }
      });        
    },
    loginHandle() {
      this.axios
        .post(`${this.settings.Host}/login/`, {
          username: this.loginForm.account,
          password: this.loginForm.checkPass
        })
        .then(response => {
          if (this.remember) {
            localStorage.user_token = response.data.token;
            localStorage.id = response.data.id;
            localStorage.username = response.data.username;
            sessionStorage.clear();
          } else {
            sessionStorage.user_token = response.data.token;
            sessionStorage.id = response.data.id;
            sessionStorage.username = response.data.username;
            localStorage.clear();
          }
          let self = this;
          this.loginPanel = false;
          this.$refs.loginForm.resetFields();
          document.getElementById("geetest1").innerHTML = "";
          this.$notify({
            title: '登录成功',
            message: '欢迎回来，路飞学成',
            type: 'success'
          });
        })
        .catch(error => {
          console.log(error)
          this.$message.error("对不起，账号密码错误");
        });
    },
    handlerPopup(captchaObj) {
      // 验证码的二次验证
      // 成功的回调
      let self = this;
      captchaObj.onSuccess(function() {
        var validate = captchaObj.getValidate();
        self.axios
          .post(`${self.settings.Host}/geetest/`, {
            geetest_challenge: validate.geetest_challenge,
            geetest_validate: validate.geetest_validate,
            geetest_seccode: validate.geetest_seccode
          })
          .then(response => {
            // 验证码验证通过，执行登录处理
            self.loginHandle();
          })
          .catch(error => {
            self.$message.error("验证码验证错误！");
          });
      });
      // 将验证码加到id为captcha的元素里
      document.getElementById("geetest1").innerHTML = ""; // 先把原来容器中的验证码清空了，在添加新的验证码
      captchaObj.appendTo("#geetest1");
    },
    get_geetest_capcha() {
      // 获取验证码
      this.axios.get(`${this.settings.Host}/geetest/`)
        .then(response => {
          // 使用initGeetest接口
          // 参数1：配置参数
          // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
          let data = response.data;
          initGeetest(
            {
              gt: data.gt,
              challenge: data.challenge,
              product: "popup", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
              offline: !data.success // 表示用户后台检测极验服务器是否宕机，一般不需要关注
            },
            this.handlerPopup
          );
        })
        .catch(error => {
          this.$message.error("获取验证码错误！");
        });
    },
    get_code () {
        // 发送短信
        if( !this.check_mobile(this.registForm.mobile) ){
            console.log("code err")
            return false;
        }
        this.axios.get(`${this.settings.Host}/sms/${this.registForm.mobile}/`).then(response=>{
            this.$message.success(response.data.message);
        }).catch(error=>{
          console.log(error)
            this.$message.error(error.response.data.message);
        });
    },
  }
};
</script>

<style lang="less" rel="stylesheet/less">
.index {
    .topbar {
        background-color: #303133;
        .container {
            .top-left {
                float: left;
                .logo {
                    float: left;
                    color: #fff;
                    line-height: 40px;
                }
                .curr-addr {
                    float: left;
                    margin-left: 20px;
                    font-size: 14px;
                    span {
                        color: #fff;
                        line-height: 40px;
                    }
                    a {
                        display: inline-block;
                        height: 22px;
                        margin: 9px 10px;
                        padding: 0 6px;
                        border-radius: 2px;
                        line-height: 22px;
                        color: #fff;
                        background-color: #2b4f6d;
                    }
                }
                .top-tabs {
                    float: left;
                    .tab-item {
                        float: left;
                        a {
                            display: inline-block;
                            padding: 0 20px;
                            height: 40px;
                            line-height: 40px;
                            color: rgb(168, 168, 168);
                            font-size: 14px;
                            &:hover {
                                color: #fff;
                            }
                        }
                        & > .active {
                            color: #fff;
                            background-color: #2b4f6d;
                        }
                    }
                }
            }
            .top-right {
                float: right;
                .top-item {
                    float: left;
                    a {
                        display: inline-block;
                        padding: 0 10px;
                        height: 40px;
                        line-height: 40px;
                        color: rgb(168, 168, 168);
                        font-size: 14px;
                        &:hover {
                            color: #fff;
                        }
                    }
                }
            }
        }
    }
    .city-list {
      .tips {
        width: 100%;
        .tips-head {
          font-size: 22px;
          margin-bottom: 20px;
        }
        .tips-desc {
          font-size: 14px;
        }
      }
      .el-dialog__body {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        .button {
          margin: 0 0 20px;
          width: 100px;
        }
      }
    }
    .el-dialog__wrapper {
      .dialog-logo {
        font-size: 40px;
        line-height: 40px;
        margin: 20px 0;
        text-align: center;
      }
        .el-dialog {
            .el-dialog__body {
                padding: 25px 50px 30px;
                .el-tabs {
                  #geetest1 {
                    .geetest_holder {
                      width: 100% !important;
                      margin-bottom: 22px;
                    }
                  }
                  .el-tabs__header {
                      padding: 0;
                      position: relative;
                      margin: 0 0 22px;
                  }
                }
                .account-btn {
                    width: 100%;
                }
            }
        }
    }
}
</style>