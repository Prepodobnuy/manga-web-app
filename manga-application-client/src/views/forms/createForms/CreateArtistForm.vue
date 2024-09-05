<script>
import fullWidthInput from '@/components/inputs/fullWidthInput.vue';
import imageInput from '@/components/inputs/imageInput.vue';
import seriousButton from '@/components/buttons/seriousButton.vue';

export default {
  name: "CreateArtistForm",
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
    <h4 class="main-h">Добавление художника</h4>
    <div class="mar-top">
      <h4>Фото</h4>
      <imageInput :image_width="250" :image_height="350" :width="166" :height="233" />
    </div>
    <div class="mar-top">
      <h4>Имя на русском</h4>
      <fullWidthInput />
    </div>
    <div class="mar-top">
      <h4>Имя на английском</h4>
      <fullWidthInput />
    </div>
    <div class="mar-top">
      <h4>Альтернативные прозвища</h4>
      <fullWidthInput previewText="вводите альтернативные прозвища разделяя символом ' / '" />
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