function validarcontacto() 
    {
      let x = document.forms["formcontacto"]["nombre"].value;
      let y = document.forms["formcontacto"]["email"].value;
      let z = document.forms["formcontacto"]["mensaje"].value;

      //todo vacío
      if ((x || y || z) == "") {
        alert("Todos los campos están vacíos!");
        return false;
      }
      // Inicio Nombre
      if ((x == "") && (y !== "") && (z !== "")) {
        alert("Ingresa Nombre");
        return false;
      }
      else {
        if ((x == "") && (y == "") && (z !== "")) {
          alert("Ingresa Nombre y Email ");
          return false;
        }
        if ((x == "") && (y !== "") && (z == "")) {
          alert("Ingresa Nombre y Mensaje");
          return false;
        }
      }
      //Fin Nombre

      // Inicio Email
      if ((x !== "") && (y == "") && (z !== "")) {
        alert("Ingresa Email");
        return false;
      }
      else {
        if ((x == "") && (y == "") && (z !== "")) {
          alert("Ingresa Nombre y Email ");
          return false;
        }
        if ((x !== "") && (y == "") && (z == "")) {
          alert("Ingresa Email y Mensaje");
          return false;
        }
      }
      //Fin Email

      // Inicio mensaje
      if ((x !== "") && (y !== "") && (z == "")) {
        alert("Ingresa Mensaje");
        return false;
      }
      else {
        if ((x == "") && (y !== "") && (z == "")) {
          alert("Ingresa Nombre y Mensaje ");
          return false;
        }
        if ((x !== "") && (y == "") && (z == "")) {
          alert("Ingresa Email y Mensaje");
          return false;
        }
      }
      //Fin mensaje


    }