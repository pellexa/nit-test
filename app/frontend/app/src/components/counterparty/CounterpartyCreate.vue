<template>
  <teleport to="body">
    <div v-if="isShow" class="wrapper-modal" @click="closeModal">
      <div class="modal-content">
        <div class="modal-title">создание контрагента</div>
        <form>
          <div class="form-row">
            <label for="name">название</label>
            <input v-model="name" id="name" type="text" />
          </div>
          <div class="form-row">
            <label for="rating">кредитный рейтинг</label>
            <input v-model="rating" id="rating" type="text" />
          </div>
          <ButtonCreate @click.prevent="create" />
        </form>
      </div>
    </div>
  </teleport>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useCounterpartiesStore } from '@/stores/counterparties'
import ButtonCreate from '../buttons/ButtonCreate.vue'

const { createCounterparty, getCounterparties } = useCounterpartiesStore()

const isShow = ref<boolean>(false)
const name = ref('')
const rating = ref('')

defineExpose({
  isShow,
})

function closeModal(event: Event) {
  if (!(event.target as HTMLElement).closest('.modal-content')) {
    isShow.value = false
  }
}

async function create() {
  await createCounterparty({ name: name.value, rating: rating.value })
  await getCounterparties()
}
</script>

<style scoped>
.wrapper-modal {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  display: inline-block;
  background-color: #fefefe;
  margin: 15% 25%;
  padding: 20px;
  border: 1px solid #888;
}

input {
  border: 1px solid black;
}
</style>
