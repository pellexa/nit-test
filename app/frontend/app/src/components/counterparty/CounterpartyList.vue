<template>
  <TheHeader />

  <SubHeader>
    <template v-slot:title><SubHeaderTitle name="контрагенты" class="subheader-title" /></template>
    <template v-slot:form>
      <SubHeaderForm>
        <template v-slot:subheader-form>
          <LocalSearch />

          <div class="group-button">
            <ButtonCreate @click="showCreateForm" /><CounterpartyCreate ref="counterpartyCreate" />
            <ButtonEdit @click="edit" />
            <ButtonDelete @click="remove" />
          </div>
        </template>
      </SubHeaderForm>
    </template>
  </SubHeader>

  <TablePlain v-if="counterparties" :content="counterparties.value" :headers="fieldMap"></TablePlain>

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
import TablePlain from '../TablePlain.vue'
import TheFooter from '../TheFooter.vue'
import CounterpartyCreate from './CounterpartyCreate.vue'
import { storeToRefs } from 'pinia'
import { useCounterpartiesStore } from '@/stores/counterparties'
import { ref } from 'vue'

const { fieldMap } = useCounterpartiesStore()
const { counterparties } = storeToRefs(useCounterpartiesStore())
const { getCounterparties } = useCounterpartiesStore()
const counterpartyCreate = ref()

getCounterparties()

function showCreateForm() {
  counterpartyCreate.value.isShow = true
}

function edit() {
  console.log('Редиктирование контрагента...')
}

function remove() {
  console.log('Удаление контрагента...')
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
</style>
