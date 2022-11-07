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

    <MenuCard title="отчёты отдела">
      <template #menu-items>
        <MenuCardItem title="сводный очтёт" class="cosolidate-report-title"><IconReportConsolidate /></MenuCardItem>
        <MenuCardItem title="EOD, EOW" class="eo-report-title"><IconReportEO /></MenuCardItem>
        <MenuCardItem title="Сводка MDP и т.д." class="summary-report-title"><IconReportSummary /></MenuCardItem>
      </template>
      <template #card-icon><IconReport /></template>
      <template #button><ButtonRightArrow title="Перейти" /></template>
    </MenuCard>

    <MenuCard title="контрагенты">
      <template #menu-items>
        <MenuCardItem title="добавление контрагентов"><IconCounterpartyAdd /></MenuCardItem>
        <MenuCardItem title="просмотр контрагентов"><IconCounterpartyView /></MenuCardItem>
        <MenuCardItem title="фильтр по контрагентам"><IconCounterpartyFilter /></MenuCardItem>
      </template>
      <template #card-icon><IconCounterparty /></template>
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
import IconReportConsolidate from '@/components/icons/cards/IconReportConsolidate.vue'
import IconReportEO from '@/components/icons/cards/IconReportEO.vue'
import IconReportSummary from '@/components/icons/cards/IconReportSummary.vue'
import IconReport from '@/components/icons/cards/IconReport.vue'
import IconCounterpartyAdd from '@/components/icons/cards/IconCounterpartyAdd.vue'
import IconCounterpartyView from '@/components/icons/cards/IconCounterpartyView.vue'
import IconCounterpartyFilter from '@/components/icons/cards/IconCounterpartyFilter.vue'
import IconCounterparty from '@/components/icons/cards/IconCounterparty.vue'
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

.cosolidate-report-title,
.eo-report-title {
  width: min-content;
}

.summary-report-title {
  width: 215px;
}
</style>
