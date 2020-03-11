<template>
  <div class="positions">
    <div class="search-panel">
      <div class="container">
        <el-row>
          <el-col :span="16" :offset="4">
            <el-input placeholder="搜索职位" v-model="searchCon">
              <template slot="append">
                <el-button>
                  <i class="el-icon-search"></i> 搜索
                </el-button>
              </template>
            </el-input>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="filter-panel">
      <div class="container">
        <div class="filter-list">
            <div class="filter-wrapper">
                <span class="label">标签 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in skillLabelsOptions" :key="id" @click="filterSkill(item)">{{ item }}</span>
                </div>
            </div>
            <div class="filter-wrapper">
                <span class="label">地区 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in cityOptions" :key="id" @click="filterCity(item)">{{ item }}</span>
                </div>
            </div>
            <div class="filter-wrapper">
                <span class="label">经验 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in workYearOptions" :key="id" @click="filterWrokYear(item)">{{ item }}</span>
                </div>
            </div>
            <div class="filter-wrapper">
                <span class="label">学历 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in educationOptions" :key="id" @click="filterEducation(id-1)">{{ item }}</span>
                </div>
            </div>
        </div>
      </div>
    </div>
    <div class="filter-require">
      <div class="container">
        <div class="require">
          <span>标签: <i v-if="filters.skillLabels">{{ filters.skillLabels }}</i><i v-else>不限</i></span>
          <span>地区: <i v-if="filters.city">{{ filters.city }}</i><i v-else>不限</i></span>
          <span>经验: <i v-if="filters.workYear">{{ filters.workYear }}</i><i v-else>不限</i></span>
          <span>学历: <i v-if="filters.education || filters.education === 0">{{ educationLabel[filters.education] }}</i><i v-else>不限</i></span>
        </div>
      </div>
    </div>
    <div class="pos-list">
      <div class="container">
        <el-row :gutter="20">
          <el-col>
            <div class="pos-item">
              <el-col :span="6" v-for="(item, index) in positions.results" :key="index">
                <router-link tag="div" :to="'position/'+item.id" class="grid-content">
                  <p class="title">
                    <span class="pos-name">{{ item.positionName }}</span>
                    <span class="pos-salary">{{ item.salary }}</span>
                  </p>
                  <p class="pos-require">
                    <span class="pos-year">{{ item.workYear }}</span> /
                    <span class="pos-edu">{{ item.education }}</span>
                  </p>
                  <p class="pos-label">
                    <span v-for="(label, id) in item.skillLabels" :key="id">{{ label }}</span>
                  </p>
                </router-link>
              </el-col>
            </div>
          </el-col>
        </el-row>
        <el-pagination
          background
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
          :page-size="16"
          :total="positions.count"
        ></el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "positions",
  data() {
    return {
        searchCon: "",
        positions: [],
        filters: {
            page: 1,
            city: '',
            workYear: '',
            education: '',
            skillLabels: ''
        },
        cityOptions: [],
        workYearOptions: [],
        educationOptions: [],
        skillLabelsOptions: [],
        educationLabel: ['小学', '初中', '高中', '大专', '本科', '硕士', '博士']
    };
  },
  created() {
    this.getPosition();
    this.PosFilterRequire();
  },
  watch: {
    "filters.page"() {
      this.getPosition();
    },
    "filters.city"() {
      this.getPosition();
    },
    "filters.workYear"() {
      this.getPosition();
    },
    "filters.education"() {
      this.getPosition();
    },
    "filters.skillLabels"() {
      this.getPosition();
    }
  },
  methods: {
    // 获取工作列表
    async getPosition() {
      let response = await this.axios.get(
        `${this.settings.Host}/home/position/`,
        {
          params: this.filters
        }
      );
      this.positions = response.data;
    },
    // 获取所有城市列表
    async PosFilterRequire () {
        let response = await this.axios.get(`${this.settings.Host}/home/PosFilterRequire/`)
        this.cityOptions = response.data.all_city
        this.workYearOptions = response.data.all_workYear
        this.skillLabelsOptions = response.data.all_skillLabels
        this.educationOptions = response.data.all_education
        this.cityOptions.unshift('不限')
        this.workYearOptions.unshift('不限')
        this.skillLabelsOptions.unshift('不限')
        this.educationOptions.unshift('不限')
    },
    // 当前页码发生改变时
    handleCurrentChange(page) {
      this.filters.page = page;
    },
    // 根据城市过滤
    filterCity (item) {
        if (item == '不限') {
            this.filters.city = '';
        } else {
            this.filters.city = item;
        }
    },
    filterWrokYear (item) {
        if (item == "不限") {
            this.filters.workYear = '';
        } else {
            this.filters.workYear = item;
        }
    },
    filterEducation (item) {
      console.log(item)
        if (item == "-1") {
            this.filters.education = '';
        } else {
            this.filters.education = item;
        }
    },
    filterSkill (item) {
        if (item == "不限") {
            this.filters.skillLabels = '';
        } else {
            this.filters.skillLabels = item;
        }
    }
  }
};
</script>

<style rel="stylesheet/less" lang="less" scoped>
.positions {
  overflow: hidden;
  .search-panel {
    background-color: #f9f9f9;
    .container {
      .el-row {
        width: 1200/16rem;
        margin: 45/16rem 0/16rem;
        .el-col {
          border-radius: 4/16rem;
        }
      }
    }
  }
  .filter-panel {
    .container {
      .filter-list {
        padding: 20/16rem 30/16rem;
        margin: 30/16rem 0;
        color: #333;
        border-radius: 8/16rem;
        background-color: #f9f9f9;
        box-shadow: 0 0 0 0 #333;
        .filter-wrapper {
            display: flex;
            justify-content: space-around;
            flex-wrap: nowrap;
            height: 36/16rem;
            .label {
                height: 30/16rem;
                line-height: 30/16rem;
                padding: 3/16rem 5/16rem;
                white-space: nowrap;
                i {
                    transition: all .5s;
                }
            }
            .item {
                display: flex;
                padding: 3/16rem;
                justify-content: flex-start;
                flex-wrap: wrap;
                flex-grow: 1;
                height: 30/16rem;
                line-height: 30/16rem;
                overflow: hidden;
                font-size: 14/16rem;
                .filter-item {
                    padding: 0 5/16rem;
                    line-height: 20/16rem;
                    height: 20/16rem;
                    margin: 5/16rem 0/16rem;
                    margin-right: 7/16rem;
                    transition: all 0.3s;
                    cursor: pointer;
                    &:hover {
                        color: #fff;
                        background-color: #005bea;
                    }
                }
            }
            &:hover {
                .item {
                    height: fit-content;
                    padding: 2/16rem;
                    max-height: 132/16rem;
                    z-index: 999;
                    background-color: rgb(255, 255, 255);
                    overflow: scroll;
                    border: 1/16rem solid #005bea;
                }
                .label {
                    background-color: #005bea;
                    color: #fff;
                    i {
                      transform: rotateZ(90deg)
                    }
                }
            }
        }
      }
    }
  }
  .filter-require {
    .container {
      .require {
        padding: 15/16rem 30/16rem;
        background-color: #f9f9f9;
        border-radius: 8/16rem;
        span {
          margin-right: 20/16rem;
          color: #333;
          i {
            border: 1/16rem dashed #005bea;
            padding: 0/16rem 3/16rem;
            color: #005bea;
            font-size: 14/16rem;
          }
        }
      }
    }
  }
  .pos-list {
    border-bottom: 1/16rem dashed #ddd;
    .container {
      .el-row {
        padding-bottom: 20/16rem;
        &:last-child {
          margin-bottom: 0;
        }
        .el-col {
          border-radius: 4/16rem;
          padding-top: 20/16rem;
          .grid-content {
            border-radius: 4/16rem;
            padding: 20/16rem;
            color: #646464;
            background-color: #fff;
            transition: all 0.3s;
            &:hover {
              box-shadow: 0 0 0.7rem 3/16rem rgba(0, 0, 0, 0.1);
              transform: translate3d(0, -0.125rem, 0);
            }
            .title {
              display: flex;
              justify-content: space-around;
              flex-wrap: nowrap;
              height: 30/16rem;
              line-height: 30/16rem;
              .pos-name {
                flex-grow: 1;
                font-weight: 400;
                color: #333;
                font-size: 20/16rem;
                text-overflow: ellipsis;
                overflow: hidden;
                white-space: nowrap;
              }
              .pos-salary {
                padding-left: 10/16rem;
                color: #dd4a38;
                font-size: 20/16rem;
                font-weight: 800;
                min-width: fit-content;
              }
            }
            .pos-require {
              height: 30/16rem;
              line-height: 30/16rem;
              font-size: 15/16rem;
            }
            .pos-label {
              text-overflow: ellipsis;
              overflow: hidden;
              white-space: nowrap;
              span {
                height: 30/16rem;
                line-height: 30/16rem;
                padding: 3/16rem 10/16rem;
                background-color: #f1f1f1;
                font-size: 12/16rem;
                border-radius: 15/16rem;
              }
              span:not(last-child) {
                margin-right: 5/16rem;
              }
            }
            .com-avatar {
              height: 80/16rem;
              text-align: center;
              img {
                width: 80/16rem;
                height: 80/16rem;
              }
            }
            .com-info {
              padding-top: 10/16rem;
              text-align: center;
              color: #646464;
              p {
                height: 30/16rem;
                line-height: 30/16rem;
                font-size: 15/16rem;
                text-overflow: ellipsis;
                overflow: hidden;
                white-space: nowrap;
              }
            }
          }
          .row-bg {
            padding: 10/16rem 10/16rem;
            background-color: #f9fafc;
          }
        }
      }
      .row-bg {
        padding: 10/16rem 0;
        background-color: #f9fafc;
      }
      .el-pagination {
        padding: 20/16rem;
        margin-bottom: 20/16rem;
        text-align: center;
      }
    }
  }
}
</style>