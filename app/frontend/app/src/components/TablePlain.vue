<template>
  <div class="wrapper-plain-table">
    <div v-if="content.length < 1" class="no-data">no data</div>
    <table v-else>
      <thead>
        <tr>
          <th v-for="(header, index) in headers" :key="header.source">
            <div class="header-wrapper">
              <div class="header-name">{{ header.target }}</div>
              <div v-if="index + 1 < headers.length" class="header-separator"></div>
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in content" :key="row.name" class="tbody-row">
          <td v-for="header in headers" :key="header">
            {{ row[header.source] }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
defineProps(['content', 'headers'])
</script>

<style scoped>
.wrapper-plain-table {
  padding: 52px 274px 127px 272px;
}
.no-data {
  font: 600 16px/1.2 Montserrat;
  margin-top: 52px;
  text-align: center;
  color: #0079c2;
}

table {
  width: 100%;
}

tr th,
tr td {
  font: 400 14px/1.5 Montserrat;
  padding: 16px 0 20px 49px;
}

.tbody-row:nth-child(odd) {
  background-color: #fff;
}

.header-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-name {
  font: 700 14px/1.5 Montserrat;
  color: #1e2832;
}

.header-name::first-letter {
  text-transform: uppercase;
}

.header-separator {
  height: 35px;
  border-right: 1px solid #b9e4ff;
  justify-self: end;
}
</style>
