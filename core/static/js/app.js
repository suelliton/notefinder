var urlBase = window.location.host;
console.log(urlBase);
if (urlBase === "127.0.0.1:8000") {
  urlBase = "http://" + urlBase;
} else {
  urlBase = "https://" + urlBase;
}

Vue.component("selectblock", {
  delimiters: ["[[", "]]"],
  template: "#select-block",
  props: {
    block: Object,
    back: String,
    search: Function
  },
  data() {
    return {};
  },
  methods: {
    mouse_in(key, state) {
      this.$emit("change-back", { key: key, state: state });
    },
    mouse_out(key, state) {
      this.$emit("change-back", { key: key, state: state });
    }
  }
});

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
      background: "",
      blocks: {
        screen: {
          label: "Screen",
          key: "screen",
          model: "None",
          values: ["None"]
        },
        ram: {
          label: "Ram",
          key: "ram",
          model: "None",
          values: ["None"]
        },
        cpu: {
          label: "Cpu",
          key: "cpu",
          model: "None",
          values: ["None"]
        },
        brand: {
          label: "Brand",
          key: "brand",
          model: "None",
          values: ["None"]
        },
        price: {
          label: "Price",
          key: "price",
          model: "None",
          values: ["None"]
        },
        storage: {
          label: "Storage",
          key: "storage",
          model: "None",
          values: ["None"]
        }
      },
      notebooks: [],

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
        for (var key in this.blocks) {
          if (this.blocks[key].model !== "None") {
            console.log(this.blocks[key].model);
            if (key === "screen" || key === "ram") {
              query_params += key + "=" + this.blocks[key].model.split(" ")[0] + "&";
            } else {
              query_params += key + "=" + this.blocks[key].model + "&";
            }
          }
        }
        console.log("query_params:" + query_params);
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
          this.blocks.screen.values.push(res.data[key].inches);
        }
      });
    },
    get_rams() {
      axios.get(urlBase + "/" + "ram").then(res => {
        for (var key in res.data) {
          this.blocks.ram.values.push(res.data[key].length);
        }
      });
    },
    get_cpus() {
      axios.get(urlBase + "/" + "cpu").then(res => {
        for (var key in res.data) {
          this.blocks.cpu.values.push(res.data[key].name);
        }
      });
    },
    get_brands() {
      axios.get(urlBase + "/" + "brand").then(res => {
        for (var key in res.data) {
          this.blocks.brand.values.push(res.data[key].name);
        }
      });
    },
    get_prices() {
      axios.get(urlBase + "/" + "price").then(res => {
        for (var key in res.data) {
          this.blocks.price.values.push(res.data[key].interval);
        }
      });
    },
    get_storages() {
      axios.get(urlBase + "/" + "storage").then(res => {
        for (var key in res.data) {
          this.blocks.storage.values.push(res.data[key].type);
        }
      });
    },
    change_background(event) {
      if (event.state) {
        this.background = "filter:blur(2px) brightness(70%);"; //aqui poderia usar ref tbm
        this.$refs[event.key].style = "opacity: 1; filter: brightness(130%);";
      } else {
        this.background = "filter:none;"; //aqui poderia usar ref tbm
        this.$refs[event.key].style = "opacity: 0;  ";
      }
    }
  }
});
