<template>
  <div class="home">
    <div class="search-panel">
      <div class="container">
        <el-row>
          <el-col :span="16" :offset="4">
              <el-input placeholder="搜索职位/公司" v-model="searchCon">
                <template slot="append"><el-button><i class="el-icon-search"></i> 搜索</el-button></template>
              </el-input>
              <div class="hots">
                <span>热门搜索: </span>
                <el-link type="primary">主要链接</el-link>
              </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="hero">
      <div class="container">
        <el-row>
          <el-col :span="5">
            <ul class="menu-wrapper">
              <li class="menu-item" v-for="item in jobs" :key=item.id>
                <span>{{ item.name }}</span>
                <a href="javascript:;">{{ item['sub_category'][0]['name'] }}</a>
                <a href="javascript:;">{{ item['sub_category'][1]['name'] }}</a>
                <i class="el-icon-arrow-right"></i>
                <div class="sub-menu">
                  <dl v-for="sub_cate in item['sub_category']" :key=sub_cate.id>
                    <dt><span>{{ sub_cate.name }}</span></dt>
                    <dd><a href="javascript:;" v-for="cate in sub_cate['category']" :key=cate.id>{{ cate.name }}</a></dd>
                  </dl>
                </div>
              </li>
            </ul>
          </el-col>
          <el-col :span="14">
            <el-carousel :interval="5000" arrow="always" height="400px">
              <el-carousel-item v-for="item in 4" :key="item">
                <h3>{{ item }}</h3>
              </el-carousel-item>
            </el-carousel> 
          </el-col>
          <el-col :span="5">
              <div class="login-panel">
                <el-avatar :size="60" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" class="demo-ruleForm">
                  <el-form-item prop="account">
                    <el-input type="text" v-model="ruleForm.account" autocomplete="off" placeholder="用户名/手机号" suffix-icon="el-icon-user"></el-input>
                  </el-form-item>
                  <el-form-item prop="checkPass">
                    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off" placeholder="密码" suffix-icon="el-icon-key"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button @click="submitForm('ruleForm')">提交</el-button>
                  </el-form-item>
                </el-form>
              </div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data () {
    var validateAccount = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入账号'));
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass');
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      }
      callback();
    };
    return {
      jobs: [],
      rec: [],
      searchCon: "",
      ruleForm: {
        account: '',
        checkPass: ''
      },
      rules: {
        account: [
          { validator: validateAccount, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.getJobs()
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    async getJobs () {
      let response = await this.axios.get(`${this.settings.Host}/home/jobs/`)
      this.jobs = response.data
      // for (let i=0; i<8; i++) {
      //   for (let j=0; j<2; i++) {
      //     let item = {};
      //     item.id = response.data[i]['sub_category'][j]['id']
      //     item.name = response.data[i]['sub_category'][j]['name']
      //   }
      //   this.rec.push(item)
      // }
    }
  }
}
</script>

<style lang="less" rel="stylesheet/less">
.home {
  height: 1000px;
  overflow: hidden;
  .search-panel {
    background-color: #f9f9f9;
    .container {
      .el-row {
        width: 1200px;
        margin: 45px 0px;
        .el-col {
          border-radius: 4px;
          .hots {
            margin-top: 10px;
            font-size: 14px;
          }
        }
      }
    }
  }
  .hero {
    margin-top: 20px;
    .container {
      .el-row {
        .el-col {
          height: 400px;
          .menu-wrapper {
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            .menu-item {
              display: flex;
              justify-content: space-between;
              padding: 0 10px;
              height: 50px;
              line-height: 50px;
              cursor: pointer;
              transition: all .3s;
              & > span {
                font-size: 16px;
                font-weight: 500;
                color: #333;
              }
              a {
                font-size: 14px;
                color: #555;
              }
              i {
                line-height: 50px;
                color: #555;
                transition: all .3s;
              }
              &:hover {
                background-color: #ecf5ff;
                & > span {
                  color: rgb(102, 177, 255);
                }
                & > a {
                  color: rgb(121, 187, 255);
                }
                & > i {
                  transform: translateX(-5px);
                  color: rgb(121, 187, 255);
                }
                .sub-menu {
                  display: block;
                }
              }
              .sub-menu {
                position: absolute;
                display: none;
                padding: 5px;
                box-sizing: border-box;
                overflow: auto;
                top: 0;
                left: 250px;
                width: 700px;
                height: 400px;
                background-color: #ecf5ff;
                z-index: 999;
                 & > dl {
                  dt {
                    height: 35px;
                    line-height: 35px;
                    font-size: 14px;
                    & > span {
                      padding: 0 15px;
                      line-height: 35px;
                    }
                  }
                  dd {
                    line-height: 35px;
                    & > a {
                      position: relative;
                      display: inline-block;
                      padding: 0 15px;
                      font-size: 14px;
                      line-height: 35px;
                      &:hover {
                        color: #2b84f1;
                      }
                      &::after {
                          content: ' ';
                          display: inline-block;
                          position: absolute;
                          height: 15px;
                          right: 0px;
                          width: 1px;
                          background-color: #989898;
                          top: 10px;
                      }
                    }
                  }
                }
              }
            }
          }
          .el-carousel__item h3 {
            color: #475669;
            font-size: 18px;
            opacity: 0.75;
            line-height: 400px;
            margin: 0;
          }
          .el-carousel__item:nth-child(2n) {
            background-color: #99a9bf;
          }
          .el-carousel__item:nth-child(2n+1) {
            background-color: #d3dce6;
          }
          .login-panel {
            height: inherit;
            padding: 20px;
            .el-avatar {
              display: flex;
              justify-content: space-around;
              margin: 0 auto;
              margin-bottom: 22px;
            }
            .el-form {
              .el-button {
                width: 100%;
              }
            }
          }
        }
      }
    }
  }
}
</style>
