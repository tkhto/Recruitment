<template>
  <div class="resume">
    <el-dropdown>
      <span class="el-dropdown-link">
        <i class="el-icon-more operate"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <li class="el-dropdown-item"><a :href="`/editresume/${item.id}`" target="_blank"><i class="el-icon-edit-outline"></i> 修改</a></li>
        <li class="el-dropdown-item" @click="removeResume(item.id)"><i class="el-icon-delete"></i> 删除</li>
      </el-dropdown-menu>
    </el-dropdown>
    <span class="file-icon">
      <i class="el-icon-document-checked"></i>
    </span>
    <p class="resume-title"><a :href="`/resume/${item.id}`" target="_blank">{{ item.title }}</a></p>
  </div>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      require: true
    },
    userInfo: {
      type: Object,
      require: true
    }
  },
  methods: {
    removeResume(resume_id) {
      this.$confirm('此操作将永久删除该简历, 是否继续?', '提示', {
        confirmButtonText: '删除',
        cancelButtonText: '留着',
        type: 'warning'
      }).then(() => {
        this.axios.delete(`${this.settings.Host}/resume_del/${resume_id}/`)
        .then(response => {
          if (response.status == 204) {
            this.$emit("removeItem");
          }
        }).catch(error => {
          console.log(error)
        })
      });
    }
  }
}
</script>

<style lang="less" rel="stylesheet">
.resume {
  position: relative;
  width: 217/16rem;
  height: 300px;
  margin-bottom: 20px;
  padding: 20px;
  box-sizing: border-box;
  border-radius: 10px;
  background-color: #fff;
  transition: all .3s;
  .el-dropdown {
    position: absolute;
    right: 20px;
    .el-dropdown-link {
      .operate {
        display: inline-block;
        padding: 5px;
        border-radius: 50%;
        color: #4ea0fd;
        background-color: white;
      } 
    }
  }
  .file-icon {
    display: block;
    padding: 30px 0;
    margin-bottom: 20px;
    text-align: center;
    color: #c3ddfa;
    transition: all .3s;
    i {
      font-size: 90px;
    }
  }
  .resume-title {
    text-align: center;
    a {
      color: #333;
    }
  }
  &:hover {
    z-index: 2;
    -webkit-box-shadow: 0 15px 30px rgba(0,0,0,.1);
    box-shadow: 0 15px 30px rgba(0,0,0,.1);
    -webkit-transform: translate3d(0,-2px,0);
    transform: translate3d(0,-2px,0);
    background-color: #c3ddfa;
    span {
      color: #fff;
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
    &:hover, &:hover > a {
      background-color: #ecf5ff;
      color: #66b1ff;
    }
  }
}
</style>