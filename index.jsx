import React from "https://esm.sh/react@19?dev";
        import ReactDOM from "https://esm.sh/react-dom@19/client?dev";
 
        ReactDOM
            .createRoot(
                document.getElementById("app")
            )
   const elem = ReactDOM.createRoot(document.getElementById("header"));
                    function tick() {
                        elem
                        .render(
                          <div>
                            <h1>Сервис получения времени</h1>
                            <h2>Текущее время {new Date().toLocaleTimeString()}.</h2>
                          </div>
                        );
                      }
                      setInterval(tick, 1000);
               
                    ReactDOM.createRoot(document.getElementById("container"))
                        .render(
                        <div>
                            <h2>Начальное время {new Date().toLocaleTimeString()}.</h2>
                        </div>
                    );


