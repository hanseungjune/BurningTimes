<template>
    <div id="footer" class="row">
      <div
        ref="scrollTopButton"
        class="invisible sticky w-full flex justify-end bottom-0 pb-3 pr-5 lg:pr-16 transition" 
        >
        <div
            class="text-gray-400 hover:text-blue-400 transition"
        >
            <button @click="scrollToTop"
                role="button"
                aria-label="scroll to top of the page" 
            > 
                <i class="bi bi-arrow-up-circle-fill"></i>
            </button>
        </div>
      </div>
      <div class="col-5" id="LOGO">LOGO</div>
      <div class="col-7" id="createdBy">@createdBy~~~~~~~~~~~~~~~~</div>
    </div>
</template>

<script>
import { defineComponent } from "vue";
import debounce from "lodash/debounce";

export default defineComponent({
        name: 'FooterFoot',
        data() {
            return {
                handleDebouncedScroll: null,
            };
        },
        mounted() {
            this.handleDebouncedScroll = debounce(this.handleScroll, 100);
            window.addEventListener("scroll", this.handleDebouncedScroll); 
        },
 
        beforeUnmount() {
            window.removeEventListener("scroll", this.handleDebouncedScroll);
        },
 
        methods: {
            handleScroll() {
                const scrollBtn = this.$refs.scrollTopButton;
 
                if (window.scrollY > 0) {
                    scrollBtn.classList.remove("invisible");
                } else {
                    scrollBtn.classList.add("invisible");
                }
            },
            scrollToTop() {
                window.scrollTo({ top: 0, behavior: "smooth" });
            },
        },
    });
</script>

<style>
#footer { 
  width: 100.7%;
  height: 100px;
  background-color: green;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

#LOGO,
#createdBy {
  font-size: 20px;
  font-weight: 900;
  color: black;
}

#LOGO {
  background-color: yellow ;
  width: 15%;
}

#createdBy {
  background-color: yellow ;
  width: 35%;
}
</style>