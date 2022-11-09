import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getEntities } from '@/composables/api-calls'
const RESTAPI = import.meta.env.VITE_RESTAPI

export const useDealsStore = defineStore('deals', () => {
  /**
   * State.
   */
  // fieldMap is not reactive.
  const fieldMap = [
    { source: 'type', target: 'тип' },
    { source: 'dateDeal', target: 'дата и вермя сделки' },
    { source: 'deliveryPoint', target: 'пункт поставки' },
    { source: 'volume', target: 'объём, МВт' },
    { source: 'price', target: ' цена, евро / МВт*ч' },
    { source: 'deliveryStart', target: 'начало поставки' },
    { source: 'deliveryEnd', target: 'конец поставки' },
    { source: 'tool', target: 'инструмент' },
    { source: 'counterparty', target: 'контрагент' },
  ]

  const deals = ref()

  /**
   * Actions.
   */
  async function getDeals() {
    const { response, request } = getEntities(`${RESTAPI}/api/v1/deals/`)

    await request()
    deals.value = response
  }

  return { fieldMap, getDeals, deals }
})
