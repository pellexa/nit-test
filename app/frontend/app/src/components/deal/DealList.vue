<template>
  <TheHeader />

  <SubHeader>
    <template v-slot:title><SubHeaderTitle name="сделки" class="subheader-title" /></template>
    <template v-slot:form>
      <SubHeaderForm>
        <template v-slot:subheader-form>
          <LocalSearch />
          <div class="wrapper-icon"><IconXls /></div>

          <div class="group-button">
            <ButtonCreate />
            <ButtonEdit @click="edit" />
            <ButtonDelete @click="remove" />
          </div>
        </template>
      </SubHeaderForm>
    </template>
  </SubHeader>

  <TablePlain v-if="deals" :content="deals.value" :headers="fieldMap"></TablePlain>

  <TheFooter />
</template>

<script setup lang="ts">
import TheHeader from '../TheHeader.vue'
import SubHeader from '../SubHeader.vue'
import SubHeaderTitle from '../SubHeaderTitle.vue'
import SubHeaderForm from '../SubHeaderForm.vue'
import LocalSearch from '../LocalSearch.vue'
import ButtonCreate from '../buttons/ButtonCreate.vue'
import ButtonEdit from '../buttons/ButtonEdit.vue'
import ButtonDelete from '../buttons/ButtonDelete.vue'
import IconXls from '../icons/IconXls.vue'
import TablePlain from '../TablePlain.vue'
import TheFooter from '../TheFooter.vue'
import { storeToRefs } from 'pinia'
import { useDealsStore } from '@/stores/deals'

const { fieldMap } = useDealsStore()
const { deals } = storeToRefs(useDealsStore())
const { getDeals } = useDealsStore()

getDeals()

function edit() {
  console.log('Редиктирование сделки...')
}

function remove() {
  console.log('Удаление сделки...')
}
</script>

<style scoped>
.subheader-title {
  margin: 51px 320px 0;
}

.group-button {
  display: flex;
  gap: 16px;
  margin-right: 48px;
}

.wrapper-icon {
  margin-right: auto;
  padding-left: 16px;
}
</style>
