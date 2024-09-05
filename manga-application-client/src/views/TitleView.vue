<script>
import accentButton from '@/components/buttons/accentButton.vue';
import axios from 'axios'

export default {
  name: "TitleView",
  components: {
    accentButton
  },
  data() {
    return {
      id: this.$route.params.id,
      data: null
    }
  },
  methods: {
    fetchData() {
      axios.get(`/title/data/${this.id}`)
        .then(response => response.json())
        .then(data => {
          this.data = data
          console.log('Fetched data:', this.data)
        })
        .catch(error => {
          console.error('Error fetching data:', error)
        })
    }
  },
  created() {
    this.fetchData()
  }
}

</script>

<template>
  <div class="ViewForm-no-bg">

    <aside>

      <div class="image-wrapper">
        <img src="" width="250" height="350">
      </div>

      <div class="buttons">
        <accentButton class="button" title="Читать" />
        <accentButton class="button" title="Оценить" />
        <accentButton class="button" title="Добавить в список" />
      </div>

      <div class="meta">
        <div class="meta-row">
          <div class="title fs-small">Формат выпуска:</div>
          <div class="data fs-default">Дурак</div>
        </div>
        <div class="meta-row">
          <div class="title fs-small">Год релиза:</div>
          <div class="data fs-default">Дурак</div>
        </div>
        <div class="meta-row">
          <div class="title fs-small">Автор:</div>
          <div class="data fs-default">Дурак</div>
        </div>
        <div class="meta-row">
          <div class="title fs-small">Художник:</div>
          <div class="data fs-default">Дурак</div>
        </div>
        <div class="meta-row">
          <div class="title fs-small">Издатель:</div>
          <div class="data fs-default">Дурак</div>
        </div>
        <div class="meta-row">
          <div class="title fs-small">Возрастной рейтинг:</div>
          <div class="data fs-default">16+</div>
        </div>
        <div class="meta-row">
          <div class="title fs-small">Загружено глав:</div>
          <div class="data fs-default">16</div>
        </div>

      </div>

    </aside>

    <main>

      <div class="name">
        <div class="main fs-giant">Человек бензочел</div>
        <div class="secondary fs-biggest">chainsaw man</div>
      </div>

      <div class="data">
      </div>

    </main>

  </div>
</template>

<style lang="scss" scoped>
* {
  color: var(--font-color);
}

.ViewForm-no-bg {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: 30px;

  aside {
    width: 250px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    gap: 13px;

    .image-wrapper {
      width: 250px;
      height: 350px;
      overflow: hidden;
      border-radius: 4px;
      user-select: none;
      -webkit-box-shadow: 0px 2px 6px 0px var(--shadow-color);
      -moz-box-shadow: 0px 2px 6px 0px var(--shadow-color);
      box-shadow: 0px 2px 6px 0px var(--shadow-color);
      background-color: var(--fg-color);

      image {
        border-radius: 4px;
      }
    }

    .buttons {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .meta {
      background-color: var(--fg-color);
      border-radius: 4px;
      padding: 4px;
      -webkit-box-shadow: 0px 2px 6px 0px var(--shadow-color);
      -moz-box-shadow: 0px 2px 6px 0px var(--shadow-color);
      box-shadow: 0px 2px 6px 0px var(--shadow-color);
      display: flex;
      flex-direction: column;
      gap: 3px;

      .meta-row {
        margin-bottom: 4px;

        .title {
          opacity: 0.8;
        }
      }
    }
  }

  main {
    width: auto;
    flex-shrink: 1;
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 13px;

    .name {
      margin-top: 5px;
      display: flex;
      flex-direction: column;

      .main {
        font-weight: 500;
      }

      .secondary {
        font-weight: 400;
      }
    }

    .data {
      border-radius: 4px;
      padding: 4px 0;
      background-color: var(--fg-color);
      width: 100%;
    }

  }
}
</style>