<template>
  <div class="wrapper-plain-table">
    <div v-if="content.length < 1" class="no-data">no data</div>
    <table v-else>
      <thead>
        <tr>
          <th class="check-mark-column"></th>
          <th v-for="(header, index) in headers" :key="header.source">
            <div class="header-wrapper">
              <div class="header-name">{{ header.target }}</div>
              <div v-if="index + 1 < headers.length" class="header-separator"></div>
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="row in content"
          :key="row.id"
          class="tbody-row"
          :class="{ 'selected-row': selectedRow.includes(row.id) }"
          @click="selectRow(row.id)"
        >
          <td class="check-mark-column">
            <div v-if="selectedRow.includes(row.id)" class="wrapper-check-mark-icon">
              <IconCheckMark />
            </div>
          </td>

          <td v-for="header in headers" :key="header">
            {{ row[header.source] }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import IconCheckMark from './icons/IconCheckMark.vue'
import { ref } from 'vue'
defineProps(['content', 'headers'])

const selectedRow = ref<number[]>([])

function selectRow(id: number) {
  if (selectedRow.value.includes(id)) {
    selectedRow.value.splice(selectedRow.value.indexOf(id), 1)
  } else {
    selectedRow.value.push(id)
  }
}
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

.check-mark-column {
  position: relative;
  width: 36px; /* 18+18 padding */
}

.wrapper-check-mark-icon {
  position: absolute;
}

tr th,
tr td {
  font: 400 14px/1.5 Montserrat;
  padding: 18px;
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

.tbody-row.selected-row {
  background-color: #def2ff;
}
</style>
