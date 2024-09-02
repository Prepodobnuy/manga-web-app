<script>
import Cropper from 'cropperjs';
import 'cropperjs/dist/cropper.css';
import accentButton from '../buttons/accentButton.vue';

export default {
    name: "imageInput",
    components: {
        accentButton
    },
    props: {
        image_width: Number,
        image_height: Number,
        width: Number,
        height: Number,
    },
    data() {
        return {
            imageSrc: null,
            editedImageSrc: null,
            editImage: false,
        };
    },
    methods: {
        imageChange(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.imageSrc = e.target.result;
                    this.editImage = true
                    this.initCropper();
                };
                reader.readAsDataURL(file);
            }
        },
        triggerImageChange() {
            this.$refs.fileInput.click();
        },
        initCropper() {
            this.$nextTick(() => {
                const image = this.$refs.image;
                this.cropper = new Cropper(image, {
                    aspectRatio: this.image_width / this.image_height,
                    viewMode: 1,
                    autoCropArea: 1,
                });
            });
        },
        getCroppedImage() {
            if (this.cropper) {
                this.editedImageSrc = this.cropper.getCroppedCanvas().toDataURL();
            }
            this.editImage = false
        },
        stopCropping() {
            this.editImage = false
        }
    }
}

</script>

<template>
    <div v-if="!editImage" class="input-wrapper" :style="{ width: width + 'px', height: height + 'px' }">
        <div class="hover" v-on:click="triggerImageChange"></div>
        <input type="file" ref="fileInput" accept="image/*" @change="imageChange" />
        <img :width="width" :height="height" :src="editedImageSrc" alt="">
    </div>
    <div v-if="editImage" class="cropper-container">
        <img ref="image" :src="imageSrc" />
    </div>
    <div v-if="editImage" class="button-row">
        <accentButton @click="getCroppedImage" title="Продолжить" />
        <accentButton @click="stopCropping" title="Отмена" />
    </div>
</template>

<style lang="scss" scoped>
.input-wrapper {
    background-color: var(--input-bg-color);
    box-shadow: 0px 0px 0px 1px var(--shadow-color);
    position: relative;
    border-radius: 4px;

    input {
        display: none;
    }

    .hover {
        width: 100%;
        height: 100%;
        cursor: pointer;
        position: absolute;
        background-color: var(--shadow-color);
        top: 0;
        left: 0;
        transition: opacity 0.2s;
        opacity: 0;

        &:hover {
            opacity: 0.5;
        }
    }
}

.cropper-container {
    width: 100%;
    height: 350px;
}

.button-row {
    margin-top: 5px;
    max-width: 450px;
    width: 100%;
    display: flex;
    flex-direction: row;
    gap: 5px;
    flex-wrap: nowrap;
}
</style>