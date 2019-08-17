Vue.component("notebook", {
  delimiters: ["[[", "]]"],
  template: "#notebook",
  props: {
    notebook: Object
  },
  data() {
    return {};
  },

  mounted() {}
  //methods: {
  // focar() {
  //   this.$refs.focus();
  // }
  // }
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
      estilo_background: "",
      estilos: {
        image1: "",
        image2: "",
        image3: "",
        image4: "",
        image5: "",
        image6: ""
      },

      telas: ["Nenhuma", "13.3 polegadas", "15 polegadas", "17 polegadas"],
      memorias: ["Nenhuma", "4 GB", "8 GB", "16 GB"],
      processadores: ["Nenhum", "i7 ", "i5 ", "i3 "],
      marcas: ["Nenhuma", "Sony ", "Acer ", "Dell "],
      precos: [
        "Nenhum",
        "500 à 2.000",
        "2.000 à 5.000",
        "5.000 à 10.000",
        "7.000 à 10.000",
        "10.000 à 50.000"
      ],

      discos: ["Nenhum", "SSD", "HDD", "Híbrido"],

      selects: {
        screen: "Nenhuma",
        ram: "Nenhuma",
        cpu: "Nenhum",
        brand: "Nenhuma",
        price: "Nenhum",
        storage: "Nenhum"
      },
      pesquisa_livre: "",
      filtros: []
    };
  },
  mounted() {},
  methods: {
    pesquisar(value) {
      if (value !== "Nenhuma" || value !== "Nenhum") {
        this.filtros.push(value);
        console.log(value);

        query_params = "";
        for (var key in this.selects) {
          if (
            this.selects[key] !== "Nenhum" &&
            this.selects[key] !== "Nenhuma"
          ) {
            console.log(this.selects[key]);
            if (key === "screen" || key === "ram") {
              query_params =
                query_params +
                key +
                "=" +
                this.selects[key].split(" ")[0] +
                "&";
            } else {
              query_params = query_params + key + "=" + this.selects[key] + "&";
            }
          }
        }
        console.log("query_params:", query_params);
        axios.get("http://127.0.0.1:8000/search?" + query_params).then(res => {
          console.log(res.data);
          this.notebooks = res.data;
        });
      }
    },
    pesquisar_livre() {
      axios
        .get(
          "http://127.0.0.1:8000/freesearch?" + "query=" + this.pesquisa_livre
        )
        .then(res => {
          console.log(res.data);
          this.notebooks = res.data;
          this.$refs.container_notebooks.click();
        });
    },
    passou_mouse(image) {
      this.estilo_background = "filter:blur(2px) brightness(70%);";
      this.estilos[image] = "opacity: 1; filter: brightness(130%);";
      /*      
            document.querySelector(".image-background").style.filter = "blur(8px)";
            document.querySelector(".image-background").style.filter = "brightness(80%)";
            document.querySelector(image).style.opacity = 1.0
            document.querySelector(image).style.filter = "brightness(120%)";*/
    },
    retirou_mouse(image) {
      this.estilo_background = "filter:none;";
      this.estilos[image] = "opacity: 0;  ";
      /*document.querySelector(".image-background").style.filter="none"
            document.querySelector(image).style.opacity = 0*/
    }
  }
});
