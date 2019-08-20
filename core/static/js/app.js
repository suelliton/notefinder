var urlBase = window.location.host;
console.log(urlBase);
if (urlBase === "127.0.0.1:8000") {
  urlBase = "http://" + urlBase;
} else {
  urlBase = "https://" + urlBase;
}

Vue.component("notebook", {
  delimiters: ["[[", "]]"],
  template: "#notebook",
  props: {
    notebook: Object
  },
  data() {
    return {};
  }
});

Vue.component("my-footer", {
  template: "#footer",
  data() {
    return {};
  }
});

new Vue({
  delimiters: ["[[", "]]"],
  el: "#app",
  data() {
    return {
      notebooks: [],
      styles: {
        background: "",
        image1: "",
        image2: "",
        image3: "",
        image4: "",
        image5: "",
        image6: ""
      },

      selects: {
        screen: "None",
        ram: "None",
        cpu: "None",
        brand: "None",
        price: "None",
        storage: "None"
      },
      sources: {
        screen: ["None"],
        ram: ["None"],
        cpu: ["None"],
        brand: ["None"],
        price: ["None"],
        storage: ["None"]
      },
      text_free_search: "",
      filters: []
    };
  },
  mounted() {
    this.load_data();
  },
  methods: {
    search(value) {
      if (value !== "None") {
        this.filters.push(value);
        console.log(value);

        query_params = "";
        for (var key in this.selects) {
          if (this.selects[key] !== "None") {
            console.log(this.selects[key]);
            if (key === "screen" || key === "ram") {
              query_params += key + "=" + this.selects[key].split(" ")[0] + "&";
            } else {
              query_params += key + "=" + this.selects[key] + "&";
            }
          }
        }
        console.log("query_params:", query_params);
        axios.get(urlBase + "/search?" + query_params).then(res => {
          console.log(res.data);
          this.notebooks = res.data;
          this.$refs.container_notebooks.click();
        });
      }
    },
    freesearch() {
      axios.get(urlBase + "/freesearch?" + "query=" + this.text_free_search).then(res => {
        console.log(res.data);
        this.notebooks = res.data;
        this.$refs.container_notebooks.click();
      });
      //limpa campos de select paraa nova pesquisa por parametro
      for (var key in this.selects) {
        this.selects[key] = "None";
      }
      this.filters = [];
    },
    load_data() {
      this.get_screens();
      this.get_rams();
      this.get_cpus();
      this.get_brands();
      this.get_prices();
      this.get_storages();
    },

    get_screens() {
      axios.get(urlBase + "/" + "screen").then(res => {
        for (var key in res.data) {
          this.sources["screen"].push(res.data[key].inches);
        }
      });
    },
    get_rams() {
      axios.get(urlBase + "/" + "ram").then(res => {
        for (var key in res.data) {
          this.sources["ram"].push(res.data[key].length);
        }
      });
    },
    get_cpus() {
      axios.get(urlBase + "/" + "cpu").then(res => {
        for (var key in res.data) {
          this.sources["cpu"].push(res.data[key].name);
        }
      });
    },
    get_brands() {
      axios.get(urlBase + "/" + "brand").then(res => {
        for (var key in res.data) {
          this.sources["brand"].push(res.data[key].name);
        }
      });
    },
    get_prices() {
      axios.get(urlBase + "/" + "price").then(res => {
        for (var key in res.data) {
          this.sources["price"].push(res.data[key].interval);
        }
      });
    },
    get_storages() {
      axios.get(urlBase + "/" + "storage").then(res => {
        for (var key in res.data) {
          this.sources["storage"].push(res.data[key].type);
        }
      });
    },
    mouse_in(image) {
      this.styles.background = "filter:blur(2px) brightness(70%);";
      this.styles[image] = "opacity: 1; filter: brightness(130%);";
      //kasdjfdasdkj
      /*      
            document.querySelector(".image-background").style.filter = "blur(8px)";
            document.querySelector(".image-background").style.filter = "brightness(80%)";
            document.querySelector(image).style.opacity = 1.0
            document.querySelector(image).style.filter = "brightness(120%)";*/
    },
    mouse_out(image) {
      this.styles.background = "filter:none;";
      this.styles[image] = "opacity: 0;  ";
      /*document.querySelector(".image-background").style.filter="none"
            document.querySelector(image).style.opacity = 0*/
    }
  }
});
