<template>
  <div class="index">
    <div class="topbar">
      <div class="container">
        <div class="top-left">
          <a class="logo" href="/home">Offend</a>
          <div class="curr-addr">
            <span>{{ curr_province }}</span>
            <a href="javascript:;" @click="changeAddrDialog = true">
              <i class="el-icon-location"></i> 切换地区
            </a>
          </div>
          <ul class="top-tabs">
            <li class="tab-item">
              <a href="javascript:;">校园招聘</a>
            </li>
            <li class="tab-item">
              <a href="javascript:;">社区</a>
            </li>
          </ul>
        </div>
        <ul class="top-right">
          <li class="top-item">
            <a :href="`createresume/${this.id}`">
              <i class="el-icon-upload"></i> 创建简历
            </a>
          </li>
          <li class="top-item" v-if="!this.token"><a href="javascript:;" @click="loginPanel = true;activeName='first'"><i class="el-icon-s-custom"></i> 登录</a></li>
          <li class="top-item" v-if="!this.token"><a href="javascript:;" @click="loginPanel = true;activeName='second'">注册</a></li>
          <li class="top-item" v-if="this.token">
            <el-dropdown>
              <span class="el-dropdown-link">
                {{ this.username }}<i class="el-icon-arrow-down el-icon--right"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <!-- 普通用户 -->
                <el-dropdown-item v-if="this.user_type==0"><router-link tag="p" to="/profile/"><i class="el-icon-s-custom"></i> 个人信息</router-link></el-dropdown-item>
                <el-dropdown-item v-if="this.user_type==0"><router-link tag="p" to="/delivery/"><i class="el-icon-s-custom"></i> 投递记录</router-link></el-dropdown-item>
                <el-dropdown-item v-if="this.user_type==0"><router-link tag="p" to="/manage/join/"><i class="el-icon-s-custom"></i> 加入公司</router-link></el-dropdown-item>
                <!-- 企业用户 -->
                <el-dropdown-item v-if="this.user_type==1"><router-link tag="p" to="/manage/"><i class="el-icon-s-custom"></i> 管理中心</router-link></el-dropdown-item>
                <el-dropdown-item v-if="this.user_type==1"><router-link tag="p" to="/received/"><i class="el-icon-s-custom"></i> 已收简历</router-link></el-dropdown-item>
                <el-dropdown-item v-if="this.user_type==1"><router-link tag="p" to="/manage/"><i class="el-icon-s-custom"></i> 找人才</router-link></el-dropdown-item>
                <el-dropdown-item><el-link :underline="false" @click="logout"><i class="el-icon-warning"></i> 退出登录</el-link></el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </li>
        </ul>
      </div>
    </div>
    <!-- 登录注册 弹出框 -->
    <el-dialog :visible.sync="loginPanel" width="30%" center>
      <h1 class="dialog-logo">Offend</h1>
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="登录" name="first">
          <el-form
            :model="loginForm"
            status-icon
            :rules="rules"
            ref="loginForm"
            class="demo-ruleForm"
          >
            <el-form-item prop="account">
              <el-input
                type="text"
                v-model="loginForm.account"
                autocomplete="off"
                placeholder="手机号"
                suffix-icon="el-icon-mobile-phone"
              ></el-input>
            </el-form-item>
            <el-form-item prop="checkPass">
              <el-input
                type="password"
                v-model="loginForm.checkPass"
                autocomplete="off"
                placeholder="密码"
                suffix-icon="el-icon-key"
              ></el-input>
            </el-form-item>
            <div id="geetest1"></div>
            <el-form-item>
              <el-button class="account-btn" @click="submitLoginForm('loginForm')">登录</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="注册" name="second">
          <el-form
            :model="registForm"
            status-icon
            :rules="rules"
            ref="registForm"
            class="demo-ruleForm"
          >
            <el-form-item prop="mobile">
              <el-input
                type="text"
                v-model="registForm.mobile"
                autocomplete="off"
                placeholder="手机号"
                suffix-icon="el-icon-mobile-phone"
              ></el-input>
            </el-form-item>
            <el-form-item prop="rpassword">
              <el-input
                type="password"
                v-model="registForm.rpassword"
                autocomplete="off"
                placeholder="密码"
                suffix-icon="el-icon-mobile-phone"
              ></el-input>
            </el-form-item>
            <el-form-item prop="sms">
              <el-input
                type="text"
                v-model="registForm.sms"
                autocomplete="off"
                placeholder="验证码"
                suffix-icon="el-icon-key"
              >
                <template slot="append">
                  <el-button type="primary" size="middle" @click="get_code()">获取验证码</el-button>
                </template>
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button class="account-btn" @click="submitRegistForm('registForm')">注册</el-button>
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
      <el-button
        v-for="item in provinceList"
        :key="item.id"
        class="button"
        @click="changeProvince(item.name)"
      >{{ item.name }}</el-button>
    </el-dialog>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from "@/components/Footer";

export default {
  data() {
    // 验证手机号
    let validateAccount = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入手机号"));
      } else if (!this.check_mobile(value)) {
        callback(new Error("手机号格式错误"));
      }
      callback();
    };
    // 验证密码
    let validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else if (value.length < 6 || value.length > 16) {
        callback(new Error("密码长度为6～16位"));
      }
      callback();
    };
    // 验证验证码
    let validateSms = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入验证码"));
      }
      callback();
    };
    return {
      token: '',
      id: '',
      username: '',
      nic_name: '',
      avatar: '',
      mobile: '',
      user_type: '',
      company_id: '',
      provinceList: [],
      curr_province: "北京市",
      activeName: "first",
      changeAddrDialog: false,
      loginPanel: false,
      searchCon: "",
      loginForm: {
        account: "",
        checkPass: ""
      },
      registForm: {
        mobile: "",
        rpassword: "",
        sms: ""
      },
      rules: {
        account: [{ validator: validateAccount, trigger: "blur" }],
        checkPass: [{ validator: validatePass, trigger: "blur" }],
        mobile: [{ validator: validateAccount, trigger: "blur" }],
        rpassword: [{ validator: validatePass, trigger: "blur" }],
        sms: [{ validator: validateSms, trigger: "blur" }]
      }
    };
  },
  created() {
    this.token = sessionStorage.user_token;
    this.id = sessionStorage.user_id;
    this.username = sessionStorage.username;
    this.nic_name = sessionStorage.nic_name;
    this.mobile = sessionStorage.mobile;
    this.avatar = sessionStorage.avatar;
    this.user_type = sessionStorage.user_type;
    this.company_id = sessionStorage.company_id;
    this.getProvince();
  },
  methods: {
    // 弹窗提示
    salert(title, message, type) {
      this.$notify({
        title: title,
        message: message,
        type: type
      });
    },
    // 校验手机号格式
    check_mobile(mobile) {
      const reg = /^1[3-9]\d{9}$/;
      if (!reg.test(mobile)) {
        return false;
      }
      return true;
    },
    // 获取省份
    async getProvince() {
      const response = await this.axios.get(
        `${this.settings.Host}/home/province/`
      );
      this.provinceList = response.data;
    },
    // 改变当前省份
    changeProvince(province) {
      this.curr_province = province;
      this.changeAddrDialog = false;
    },
    handleClick(tab, event) {
      // console.log(tab, event);
    },
    // 登录处理
    submitLoginForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.get_geetest_capcha();
        } else {
          return false;
        }
      });
    },
    // 注册处理
    submitRegistForm(formName) {
      // 验证数据
      this.$refs[formName].validate(valid => {
        if (valid) {
          // 提交数据
          this.axios
            .post(`${this.settings.Host}/`, {
              mobile: this.registForm.mobile,
              password: this.registForm.rpassword,
              sms_code: this.registForm.sms
            })
            .then(response => {
              // 注册成功!保存登录状态
              sessionStorage.user_id = response.data.id;
              sessionStorage.user_name = response.data.username;
              sessionStorage.user_token = response.data.token;
              sessionStorage.mobile = response.data.mobile;
              sessionStorage.avatar = response.data.avatar;
              sessionStorage.nic_name = response.data.nic_name;
              sessionStorage.user_type = response.data.user_type;
              sessionStorage.company_id = response.data.companyId;
              this.token = response.data.token;
              this.id = response.data.id;
              this.username = response.data.username;
              this.nic_name = response.data.nic_name;
              this.avatar = response.data.avatar;
              this.mobile = response.data.mobile;
              this.user_type = response.data.user_type;
              this.company_id = response.data.companyId;
              let self = this;
              this.salert("注册成功", "在这里寻找你的新起点吧", "success");
              this.loginPanel = false;
              this.$refs.registForm.resetFields();
            })
            .catch(error => {
              console.log(error);
              this.salert("注册失败", "请求发送失败", "error");
            });
        } else {
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
          sessionStorage.user_token = response.data.token;
          sessionStorage.user_id = response.data.id;
          sessionStorage.username = response.data.username;
          sessionStorage.mobile = response.data.mobile;
          sessionStorage.avatar = response.data.avatar;
          sessionStorage.nic_name = response.data.nic_name;
          sessionStorage.user_type = response.data.user_type;
          sessionStorage.company_id = response.data.companyId;
          this.token = response.data.token;
          this.id = response.data.id;
          this.username = response.data.username;
          this.nic_name = response.data.nic_name;
          this.avatar = response.data.avatar;
          this.mobile = response.data.mobile;
          this.user_type = response.data.user_type;
          this.company_id = response.data.companyId;
          let self = this;
          this.loginPanel = false;
          this.$refs.loginForm.resetFields();
          document.getElementById("geetest1").innerHTML = "";
          this.salert("登录成功", "欢迎回来～", "success");
        })
        .catch(error => {
          this.salert("登录失败", "请重新尝试", "error");
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
            this.salert("验证失败", "信号丢失了，请重试", "error");
          });
      });
      // 将验证码加到id为captcha的元素里
      document.getElementById("geetest1").innerHTML = ""; // 先把原来容器中的验证码清空了，在添加新的验证码
      captchaObj.appendTo("#geetest1");
    },
    get_geetest_capcha() {
      // 获取验证码
      this.axios
        .get(`${this.settings.Host}/geetest/`)
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
          this.salert("请求失败", "请重试", "error");
        });
    },
    get_code() {
      // 发送短信
      if (!this.check_mobile(this.registForm.mobile)) {
        // 检查手机号格式
        return false;
      }
      this.axios
        .get(`${this.settings.Host}/sms/`, {
          params: {
            mobile: this.registForm.mobile,
            tpl: 'register'
          }
        })
        .then(response => {
          if (response.data.status == 0) {
            this.salert("请求成功", response.data.message, "success");
          } else {
            this.salert("请求失败", response.data.message, "error");
          }
        })
        .catch(error => {
          this.salert("获取失败", "请重试", "error");
        });
    },
    logout () {
      sessionStorage.clear();
      location.href="/home"
    }
  },
  components: {
    Footer
  }
};
</script>

<style lang="less" rel="stylesheet/less">
.index {
  min-width: 1200/16rem;
  .topbar {
    background-color: #fff;
    box-shadow: 0 0 12/16rem 0/16rem #fff;
    border-bottom: 3px solid #ddd;
    .container {
      .top-left {
        float: left;
        .logo {
          float: left;
          color: #333;
          line-height: 40/16rem;
        }
        .curr-addr {
          float: left;
          margin-left: 20/16rem;
          font-size: 14/16rem;
          span {
            color: #333;
            line-height: 40/16rem;
          }
          a {
            display: inline-block;
            height: 22/16rem;
            margin: 9/16rem 10/16rem;
            padding: 0 6/16rem;
            border-radius: 2/16rem;
            line-height: 22/16rem;
            color: #333;
            background-color: #eee;
          }
        }
        .top-tabs {
          float: left;
          .tab-item {
            float: left;
            a {
              display: inline-block;
              padding: 0 20/16rem;
              height: 40/16rem;
              line-height: 40/16rem;
              color: #333;
              font-size: 14/16rem;
              &:hover {
                color: #333;
              }
            }
            & > .active {
              color: #333;
              background-color: #2b4f6d;
            }
          }
        }
      }
      .top-right {
        float: right;
        .top-item {
          float: left;
          transition: all .3s;
          .el-dropdown-link {
            line-height: 40px;
            cursor: pointer;
            color: #333;
            .el-icon-arrow-down {
              font-size: 12px;
            }
          }
          a {
            display: inline-block;
            padding: 0 10/16rem;
            height: 40/16rem;
            line-height: 40/16rem;
            color: #333;
            font-size: 14/16rem;
            &:hover {
              color: #333;
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
        font-size: 22/16rem;
        margin-bottom: 20/16rem;
      }
      .tips-desc {
        font-size: 14/16rem;
      }
    }
    .el-dialog__body {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      .button {
        margin: 0 0 20/16rem;
        width: 100/16rem;
      }
    }
  }
  .el-dialog__wrapper {
    .dialog-logo {
      font-size: 40/16rem;
      line-height: 40/16rem;
      margin: 20/16rem 0;
      text-align: center;
    }
    .el-dialog {
      .el-dialog__body {
        padding: 25/16rem 50/16rem 30/16rem;
        .el-tabs {
          #geetest1 {
            .geetest_holder {
              width: 100% !important;
              margin-bottom: 22/16rem;
            }
          }
          .el-tabs__header {
            padding: 0;
            position: relative;
            margin: 0 0 22/16rem;
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
