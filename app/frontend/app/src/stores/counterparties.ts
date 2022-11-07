import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { CounterpartyType } from '@/types/entities-types'
import { getEntities, createEntities } from '@/composables/api-calls'
const RESTAPI = import.meta.env.VITE_RESTAPI

export const useCounterpartiesStore = defineStore('counterparties', () => {
  /**
   * State.
   */
  // fieldMap is not reactive.
  const fieldMap = [
    { source: 'name', target: 'кантрагенты' },
    { source: 'rating', target: 'цена закрытия' },
  ]

  const counterparties = ref()

  /**
   * Actions.
   */
  async function getCounterparties() {
    // const { response, request } = getEntities('http://127.0.0.1:8000/api/v1/counterparties/')
    const { response, request } = getEntities(`${RESTAPI}/api/v1/counterparties/`)

    await request()
    counterparties.value = response
  }

  async function createCounterparty(data: CounterpartyType) {
    const { response, request } = createEntities(`${RESTAPI}/api/v1/counterparties/`, data)

    await request()
    counterparties.value = response
  }

  return { fieldMap, getCounterparties, createCounterparty, counterparties }
})
