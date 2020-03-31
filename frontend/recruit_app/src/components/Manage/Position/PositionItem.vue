<template>
  <div class="position">
    <div class="header">
      <div class="position-info">
        <span class="name">
          <a :href="`/position/${item.id}`" target="_blank">{{ item.positionName }}</a>
        </span>
        <span class="pub-date">发布时间：{{ item.create_time | dateStr }}</span>
      </div>
      <el-dropdown class="more-operate" trigger="click" @command="handleCommand">
        <span class="el-dropdown-link">
          <i class="fa fa-ellipsis-v"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <li class="el-dropdown-item">
            <a :href="`/editposition/${item.id}`" target="_blank">
              <i class="el-icon-edit-outline"></i> 修改
            </a>
          </li>
          <li class="el-dropdown-item" @click="removePosition(item.id)">
            <i class="el-icon-delete"></i> 删除
          </li>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <div class="footer">
      <span>投递人数 0</span>
    </div>
  </div>
</template>

<script>
import moment from "moment";

export default {
  data() {
    return {};
  },
  props: {
    item: {
      type: Object,
      require: true
    }
  },
  filters: {
    dateStr: function(value, format = "YYYY-MM-DD HH:mm:ss") {
      return moment(value).format(format);
    }
  },
  methods: {
    handleCommand(command) {
      this.axios
        .delete(`${this.settings.Host}/news_del/${command}/`)
        .then(response => {
          if (response.status == 204) {
            this.$emit("removeItem");
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    removePosition (position_id) {
      this.$confirm("此操作将永久删除该招聘职位信息, 是否继续?", "提示", {
        confirmButtonText: "删除",
        cancelButtonText: "留着",
        type: "warning"
      }).then(() => {
        this.axios
          .delete(`${this.settings.Host}/home/position/delete/${position_id}/`)
          .then(response => {
            if (response.status == 204) {
              this.$emit("removeItem");
            }
          })
          .catch(error => {
            console.log(error);
          });
      });
    }
  }
};
</script>
<style lang="less" rel="stylesheet/less">
.position {
  width: 100%;
  background-color: #fff;
  padding: 0px 20px 10px;
  border-radius: 10px;
  margin-bottom: 20px;
  .header {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    .position-info {
      display: flex;
      justify-content: space-between;
      flex-grow: 1;
      padding-left: 10px;
      span {
        line-height: 50px;
        margin-right: 10px;
      }
      .name {
        a {
          font-weight: 900;
          color: #333;
          font-size: 18px;
          &:hover {
            color: #0c90fd;
          }
        }
      }
      .pub-date {
        font-size: 14px;
        color: #999;
      }
    }
    .more-operate {
      display: inline-block;
      width: 20px;
      text-align: center;
      line-height: 50px;
      i {
        padding: 5px 10px;
        transition: all 0.3s;
        &:hover {
          background-color: #eee;
          border-radius: 5px;
        }
      }
    }
  }

  .footer {
    border-top: 1px solid #e2e2e2;
    padding-top: 10px;
    span {
      display: inline-block;
      width: 100px;
      padding: 0 10px;
      color: #666;
    }
  }
}
.el-dropdown-menu {
  .el-dropdown-item {
    padding: 5px 20px;
    text-align: center;
    font-size: 14px;
    color: #666;
    cursor: pointer;
    a {
      color: #666;
    }
    &:hover {
      background-color: #ecf5ff;
      color: #66b1ff;
      a {
        background-color: #ecf5ff;
        color: #66b1ff;
      }
    }
  }
}
</style>