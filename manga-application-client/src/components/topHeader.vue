<script>
import navButton from '@/components/buttons/navButton.vue'
import squareNavButton from '@/components/buttons/squareNavButton.vue'
import popupNewObjectMenu from '@/components/popupMenus/popupNewObjectMenu.vue'
import popupNotificationMenu from '@/components/popupMenus/popupNotificationMenu.vue'
import popupColorThemeMenu from './popupMenus/popupColorThemeMenu.vue'
import TopSearchBar from '@/components/TopSearchBar.vue'
import IconHome from './icons/IconHome.vue'

export default {
    name: "topHeader",
    props: {
        name: String
    },
    components: {
        navButton,
        squareNavButton,
        popupNewObjectMenu,
        popupNotificationMenu,
        popupColorThemeMenu,
        TopSearchBar,
        IconHome
    },
    data() {
        return {
            showCreatePopup: false,
            showNotifyPopup: false,
            showColorThemePopup: false,
            showSearchField: false,
        }
    },
    watch: {
        showSearchField(value) {
            if (value) {
                console.log("true")
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        }
    },
    methods: {
        showCreatePopupClick() {
            this.showCreatePopup = !this.showCreatePopup
            this.showNotifyPopup = false
            this.showColorThemePopup = false
        },
        showNotifyPopupClick() {
            this.showNotifyPopup = !this.showNotifyPopup
            this.showCreatePopup = false
            this.showColorThemePopup = false
        },
        showColorThemePopupClick() {
            this.showColorThemePopup = !this.showColorThemePopup
            this.showNotifyPopup = false
            this.showCreatePopup = false
        },
        showSearchFieldClick() {
            this.hideAll()
            this.showSearchField = true
        },
        hideSearchFieldClick() {
            this.showSearchField = false
        },
        hideAll() {
            this.showCreatePopup = false
            this.showNotifyPopup = false
            this.showColorThemePopup = false
        }
    }
}
</script>

<template>
    <transition name="bg-dimm">
        <div v-if="showSearchField" v-on:click="hideSearchFieldClick" class="bg-dimm"></div>
    </transition>
    <header class="top-header">
        <div class="caption">
            <RouterLink class="main-link" to="/"> <IconHome class="icon-home" /> Манга</RouterLink>
            <nav>
                <RouterLink to="/catalog">
                    <navButton title="Каталог" leftD="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                </RouterLink>

                <navButton v-on:click="showSearchFieldClick" title="Поиск"
                    leftD="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />

                <RouterLink to="/randomtitle">
                    <navButton title="Рандом"
                        leftD="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 0 0-3.7-3.7 48.678 48.678 0 0 0-7.324 0 4.006 4.006 0 0 0-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 0 0 3.7 3.7 48.656 48.656 0 0 0 7.324 0 4.006 4.006 0 0 0 3.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3-3 3" />
                </RouterLink>
            </nav>
            <div class="w100"></div>
            <div class="popup-menu-place">
                <squareNavButton v-on:click="showColorThemePopupClick"
                    d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
                <transition name="modal-fade">
                    <popupColorThemeMenu v-if="showColorThemePopup" />
                </transition>
            </div>
            <div class="popup-menu-place">
                <squareNavButton v-on:click="showCreatePopupClick" d="M12 4.5v15m7.5-7.5h-15" />
                <transition name="modal-fade">
                    <popupNewObjectMenu @hideAll="hideAll" v-if="showCreatePopup" />
                </transition>
            </div>
            <div class="popup-menu-place">
                <squareNavButton v-on:click="showNotifyPopupClick"
                    d="M14.857 17.082a23.848 23.848 0 0 0 5.454-1.31A8.967 8.967 0 0 1 18 9.75V9A6 6 0 0 0 6 9v.75a8.967 8.967 0 0 1-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 0 1-5.714 0m5.714 0a3 3 0 1 1-5.714 0" />
                <transition name="modal-fade">
                    <popupNotificationMenu v-if="showNotifyPopup" />
                </transition>
            </div>

            <squareNavButton
                d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
        </div>
    </header>
    <transition name="searchFieldTransition">
        <TopSearchBar v-if="showSearchField" />
    </transition>
</template>


<style lang="scss">
.bg-dimm {
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1999;
    background-color: rgba(0, 0, 0, 0.25);
}

header.top-header {
    position: fixed;
    height: 56px;
    width: 100vw;
    background-color: var(--fg-color);
    z-index: 1000;
    top: 0;
    left: 0;
    -webkit-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    -moz-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    box-shadow: 0px 2px 6px 0px var(--shadow-color);

    .caption {
        height: 100%;
        margin-left: auto;
        margin-right: auto;
        display: flex;
        align-items: center;

        .main-link {
            font-weight: 600;
            user-select: none;
            font-size: 2.2ch;
            user-select: none;
            display: flex;
            flex-direction: row;
            flex-wrap: nowrap;
            align-items: center;
            cursor: pointer;
            transition: color 0.2s;

            &:hover {
                color: var(--accent-font-hover);
                .icon-home {
                    transition: fill 0.2s;
                    .fill {
                        fill:var(--accent-font-hover);
                    }
                    .border {
                        fill:var(--accent-font-hover);
                    }
                }
            }

            &:active {
                color: var(--accent-font-active);
                .icon-home {
                    .fill {
                        fill:var(--accent-font-active);
                    }
                    .border {
                        fill:var(--accent-font-active);
                    }
                }
            }
        }

        nav {
            position: absolute;
            display: flex;
            gap: 4px;
            left: 50%;
            transform: translate(-50%, 0);
        }

        .w100 {
            width: 100%;
        }

        .popup-menu-place {
            position: relative;
            width: 36px;
            height: 36px;
        }
    }
}

.modal-fade-enter-active,
.modal-fade-leave-active {
    transition: opacity 0.2s, transform 0.3s;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
    opacity: 0;
    transform: translate(10px, 0px);
}

.modal-fade-enter-to,
.modal-fade-leave-from {
    opacity: 1;
}


.searchFieldTransition-enter-active,
.searchFieldTransition-leave-active {
    transition: opacity 0.2s;
}

.searchFieldTransition-enter-from,
.searchFieldTransition-leave-to {
    opacity: 0;
}

.searchFieldTransition-enter-to,
.searchFieldTransition-leave-from {
    opacity: 1;
}


.bg-dimm-enter-active,
.bg-dimm-leave-active {
    transition: opacity 0.4s, transform 0.5s;
}

.bg-dimm-enter-from,
.bg-dimm-leave-to {
    opacity: 0;
}

.bg-dimm-enter-to,
.bg-dimm-leave-from {
    opacity: 1;
}
</style>