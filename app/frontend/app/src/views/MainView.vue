<template>
  <TheHeader />
  <SubHeader>
    <template #form><TheSearch class="main-search" /></template>
  </SubHeader>

  <div class="menu-cards">
    <MenuCard title="база сделок">
      <template #menu-items>
        <MenuCardItem title="просмотр сделок"><IconViewDeal /></MenuCardItem>
        <MenuCardItem title="добавление сделок"><IconAddDeal /></MenuCardItem>
        <MenuCardItem title="фильтр по сделкам"><IconFilterDeal /></MenuCardItem>
      </template>
      <template #card-icon><IconDeal /></template>
      <template #button><ButtonRightArrow title="Изучить" /></template>
    </MenuCard>
  </div>

  <TheFooter />
</template>

<script setup lang="ts">
import TheHeader from '@/components/TheHeader.vue'
import SubHeader from '@/components/SubHeader.vue'
import TheSearch from '@/components/TheSearch.vue'
import MenuCard from '@/components/layouts/cards/MenuCard.vue'
import MenuCardItem from '@/components/layouts/cards/MenuCardItem.vue'
import IconViewDeal from '@/components/icons/cards/IconViewDeal.vue'
import IconAddDeal from '@/components/icons/cards/IconAddDeal.vue'
import IconFilterDeal from '@/components/icons/cards/IconFilterDeal.vue'
import IconDeal from '@/components/icons/cards/IconDeal.vue'
import ButtonRightArrow from '@/components/buttons/ButtonRightArrow.vue'
import TheFooter from '@/components/TheFooter.vue'
</script>

<style scoped>
.main-search {
  margin: 66px 320px 0;
}

.menu-cards {
  display: flex;
  gap: 24px;
  margin: 0 320px;
  transform: translate(0, -142px);
}
</style>
