<script>
export default {
  name: "tagSelect",
  created() { },
  data() {
    return {
      selectedTags: [],
      showHints: false
    };
  },
  components: {
  },
  props: {
    tags: Array, // [ {id: 0, name:"as"}, {id: 1, name:"as"} ]
    title: String
  },
  methods: {
    showHint() {
      this.showHints = true;
      this.inputHandler()
    },
    hideHint() {
      this.showHints = false;
    },
    inputHandler() {
      let text = this.$refs.input.value
      this.fillHintColumn(text)
    },
    clearHintColumn() {
      this.$refs.hintColumn.innerHTML = '';
    },
    fillHintColumn(substring) {
      let sortedTags = []
      this.tags.forEach(tag => {
        if (tag.name.includes(substring)) {
          sortedTags.push(tag)
        }
      });

      const filteredList = sortedTags.filter(item1 =>
        !this.selectedTags.some(item2 => item2.id === item1.id)
      );

      if (this.$refs.hintColumn) {
        this.clearHintColumn()

        filteredList.forEach(tag => {
          let button = document.createElement('button');
          button.innerText = tag.name;
          button.classList.add('hint-button');
          button.classList.add('fs-default');
          button.onclick = () => {
            this.selectTag(tag);
          };
          this.$refs.hintColumn.appendChild(button);
        });
      }
    },
    selectTag(tag) {
      this.selectedTags.push(tag)

      this.inputHandler()

      let button = document.createElement('button');
      button.innerText = tag.name;
      button.classList.add('selected-hint-button');
      button.classList.add('fs-default');
      button.onclick = () => {
        this.unselectTag(tag);
        button.remove()
      };
      this.$refs.selectedHits.appendChild(button)

    },
    unselectTag(tag) {
      this.selectedTags = this.selectedTags.filter(item => item !== tag);
      this.fillHintColumn('')
    }

  },
};
</script>

<template>
  <div class="buttons">
    <h4>{{ title }}</h4>
    <div class="margin-left">
      <button v-if="!showHints" class="btn" @click="showHint"> 
          <svg xmlns="http://www.w3.org/2000/svg" fill="none"
          viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="size-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
        </svg>

      </button>
      <button v-if="showHints" @click="hideHint" class="btn"> 
          <svg xmlns="http://www.w3.org/2000/svg" fill="none"
          viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="size-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
  </div>
  <div ref="selectedHits" class="selected-hits">
  </div>

  <div class="wrapper">
    <div v-if="showHints" class="hint-menu">
      <input v-on:input="inputHandler" ref="input" type="text">
      <div ref="hintColumn" class="hint-column">
      </div>
    </div>

  </div>

</template>


<style lang="scss" scoped>
.buttons {
  display: flex;
  flex-direction: row;
  gap: 4px;
  align-items: center;

  .margin-left {
    margin-left: auto;
  }
}

.selected-hits {
  display: flex;
  flex-direction: row;
  gap: 4px;
  flex-wrap: wrap;
}

svg {
        width: 20px;
        height: 20px;
        stroke: var(--accent-font);
    }
.wrapper {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;

  .hint-menu {
    width: 100%;
    height: 300px;
    position: absolute;
    box-shadow: 0px 0px 0px 1px var(--shadow-color);
    background-color: var(--input-bg-color);
    top: 100%;
    left: 0;
    z-index: 100;
    border-radius: 2px;
    display: flex;
    flex-direction: column;

    .btn {
      position: absolute;
      right: 0;
    }


    input {
      border: unset;
      outline: unset;
      z-index: 100;
      width: 100%;
      height: 30px;
      font-size: medium;
      border-radius: 2px 2px 0px 0px;
      background-color: var(--input-bg-color);
      box-shadow: 0px 0px 0px 1px var(--shadow-color);
    }

    .hint-column {
      z-index: 99;
      min-height: 0px;
      height: min-content;
      max-height: 269px;
      overflow-y: auto;
    }
  }
}


.btn {
  width: 30px;
  height: 30px;
  border: unset;
  outline: unset;
  background-color: unset;
  cursor: pointer;
  transition: transform 0.1s;

  &:hover {
    transform: translateY(2px);
  }

  &:active {
    transform: scale(0.9);
  }

}
</style>