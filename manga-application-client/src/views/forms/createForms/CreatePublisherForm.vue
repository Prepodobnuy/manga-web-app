<script>
import fullWidthInput from '@/components/inputs/fullWidthInput.vue';
import imageInput from '@/components/inputs/imageInput.vue';
import seriousButton from '@/components/buttons/seriousButton.vue';

export default {
  name: "CreatePublisherForm",
  components: {
    fullWidthInput,
    imageInput,
    seriousButton
  },
  created() { },
  data() {
    return {};
  },
  props: {},
  methods: {},
};
</script>

<template>
  <div class="ThinViewForm">
    <h4 class="main-h">Добавление издательства</h4>
    <div class="mar-top">
      <h4>Фото</h4>
      <imageInput :image_width="250" :image_height="350" :width="166" :height="233" />
    </div>
    <div class="mar-top">
      <h4>Оригинальное название</h4>
      <fullWidthInput />
    </div>
    <div class="mar-top">
      <h4>Русское название</h4>
      <fullWidthInput />
    </div>
    <div class="mar-top">
      <h4>Английское название</h4>
      <fullWidthInput />
    </div>
    <div class="mar-top">
      <h4>Альтернативные названия</h4>
      <fullWidthInput previewText="вводите альтернативные названия разделяя символом ' / '" />
    </div>
    <div class="button-row mar-top">
      <seriousButton title="Отмена" />
      <seriousButton title="Добавить" />
    </div>

  </div>
</template>


<style lang="scss" scoped>
.mar-top {
  margin-top: 30px;

  h4 {
    position: relative;
    margin-bottom: 8px;
    display: flex;
    flex-wrap: nowrap;

    .right {
      position: absolute;
      right: 0;
      font-size: medium;
    }
  }
}

.button-row {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: 30px;
}
</style>