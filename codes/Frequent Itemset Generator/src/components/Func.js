import React from 'react'
import axios from 'axios';

export default function Func() {
    const [count, setCount] = React.useState(4);
    const addRow = () => {
         setCount(count + 1);
        let div_mb3 = document.createElement("div");
        div_mb3.className = "mb-3";
        let input = document.createElement("input");
        input.setAttribute("type", "text");
        input.setAttribute("class", "form-control");
        input.setAttribute("id", "exampleFormControlInput1");
        input.setAttribute("placeholder",`T${count}`);
        div_mb3.appendChild(input);
        let container = document.getElementById("container");
        container.appendChild(div_mb3);

    }
    const removeRow = () => {
        if(count > 1){
            setCount(count - 1);
            let container = document.getElementById("container");
            container.removeChild(container.lastChild);
        }
    }



    const handleSubmit = async (e)  => {
        e.preventDefault();
        let data = {};
        let container = document.getElementById("container");
        let fields = container.getElementsByTagName("input");
        let minSup = document.getElementById("minSup").value;
        let minConf = document.getElementById("minConf").value;
        let result = document.getElementById("result");
        
        for(let i = 0; i < fields.length; i++){
            data[fields[i].placeholder] = String(fields[i].value).split(" ");
        }

        // alert(JSON.stringify(data));
        await axios.post(`https://somethinginaway.herokuapp.com/get${minSup}&${minConf}`, data)
        .then(res => {
            let h1 = document.createElement("h1");
            h1.innerHTML = "Transactions";
            h1.style.marginBottom = "25px"
            result.appendChild(h1);
            

            

            let freq = res.data.freq;
            let table = document.createElement("table");
            table.className = "table table-dark table-striped";
            let thead = document.createElement("thead");
            let tr = document.createElement("tr");
            let th = document.createElement("th");
            
            th = document.createElement("th");
            // th.className = "text-start"
            th.innerHTML = "Tid";
            tr.appendChild(th);
            th = document.createElement("th");
            th.innerHTML = "Transactions";
            th.className = "text-start"
            tr.appendChild(th);
            thead.appendChild(tr);
            table.appendChild(thead);
            let count = 1;
            for(let i = 0; i < fields.length; i++){
                let tr = document.createElement("tr");
                tr.className = "table-success"
                let td = document.createElement("td");
                
                td = document.createElement("td");
                td.innerHTML = fields[i].placeholder;
                td.setAttribute("scope","row")
                tr.appendChild(td);
                td = document.createElement("td");
                td.innerHTML = fields[i].value;
                td.className="text-start"
                td.setAttribute("scope","row")
                tr.appendChild(td);
                table.appendChild(tr);
            }
            result.appendChild(table);
            h1 = document.createElement("h1");
            h1.innerHTML = "Itemset";
            h1.style.marginBottom = "25px"
            result.appendChild(h1);


            let table2 = document.createElement("table");
            table2.className = "table table-dark table-striped";
            let thead2 = document.createElement("thead");
            let tr2 = document.createElement("tr");
            let th2 = document.createElement("th");
            
            th2 = document.createElement("th");
            // th.className = "text-start"
            th2.innerHTML = "#";
            tr2.appendChild(th2);
            th2 = document.createElement("th");
            th2.innerHTML = "Items";
            th2.className = "text-start"
            tr2.appendChild(th2);
            th2 = document.createElement("th");
            th2.innerHTML = "Frequency";
            tr2.appendChild(th2);
            thead2.appendChild(tr2);
            table2.appendChild(thead2);

            for(let [key,value] of Object.entries(freq)){

                let tr = document.createElement("tr");
                tr.className = "table-success"
                let td = document.createElement("td");
                td.className = "table-success"
                td.innerHTML = count
                td.setAttribute("scope","row")
                tr.appendChild(td)
                td = document.createElement("td");
                td.innerHTML = key;
                td.className="text-start"
                td.setAttribute("scope","row")
                tr.appendChild(td);
                td = document.createElement("td");
                td.innerHTML = value;
                td.setAttribute("scope","row")
                tr.appendChild(td);
                table2.appendChild(tr);
                count++;
            }
            result.appendChild(table2);
            // result.innerHTML = `<h1 style={{
            //     marginBottom: '25px',
            // }}> Itemset</h1>`;
            
            h1 = document.createElement("h1");
            h1.innerHTML = "Rules";
            h1.style.marginBottom = "25px"
            result.appendChild(h1);

            let data = res.data["rules"];
            console.log(data.length);
            for (let i = 0; i < data.length; i++) {
                let result = document.getElementById("result")
                // console.log(data[i][0][0], data[i][0][1], data[i][1]);
            // result[fields[i].placeholder] = String(fields[i].value).split(" ");
            let alert = document.createElement('div');
            alert.setAttribute("role","alert")
            if (data[i][1]>0.6){
                alert.className = "alert alert-success text-start";
                alert.innerHTML = `${data[i][0][0]} -> ${data[i][0][1]} : ${data[i][1]}`;
            }
            else{
                alert.className = "alert alert-danger text-start";
                alert.innerHTML = `${data[i][0][0]} -> ${data[i][0][1]} : ${data[i][1]}`;
            }
            result.appendChild(alert);
        }
        
        // console.log(res);
        })
        .catch(err => {
            console.log(err);
        })
    }
    // const printFields = () => {
    //     let container = document.getElementById("container");
    //     let fields = container.getElementsByTagName("input");
    //     let result = document.getElementById("result")
    //     for(let i = 0; i < fields.length; i++){
    //         // result[fields[i].placeholder] = String(fields[i].value).split(" ");
    //         let alert = document.createElement('div');
    //         alert.className = "alert alert-success text-start";
    //         alert.setAttribute("role","alert")
    //         alert.innerHTML = `${String(fields[i].value).split(" ")}`
    //         result.appendChild(alert);
    //     }
    //     // alert(JSON.stringify(result));
    // }
    const loadData = () => {
        let data = ["apple beer rice chicken",
        "apple beer rice",
        "apple beer" ,
        "milk beer rice chicken",
        "apple mango",
        "milk beer rice" ,
        "milk beer",
        "milk mango"]
        let container = document.getElementById("container");
        let fields = container.getElementsByTagName("input");
        
        for(let i = 0; i < fields.length; i++){
            fields[i].value = data[i];
        }
        let minSup = document.getElementById("minSup")
        let minConf = document.getElementById("minConf")
        minSup.value = "2";
        minConf.value = "0.6";
    }

    const clear = () => {
        let container = document.getElementById("container");
        let fields = container.getElementsByTagName("input");
        let result = document.getElementById("result")
        let minConf = document.getElementById("minConf")
        let minSup = document.getElementById("minSup")
        minConf.value = "";
        minSup.value = "";
        
        for(let i = 0; i < fields.length; i++){
            fields[i].value = "";
        }
        result.innerHTML = "";
        
        
    }

    const btns ={
        margin : "10px"
    
    }
      return (
    <>
    <div id='container' className='container' style={{
        marginTop: '50px',
    }}>
        <h1 style={{
        marginBottom: '25px',
    }}> Frequent Item Set Generator </h1>
    <div class="mb-3">
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="T1" />
    </div>
    <div class="mb-3">
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="T2" />
    </div>
    <div class="mb-3">
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="T3" />
    </div>
    </div>
    <div className='values' style={{
        marginBottom: '20px',
        display:"flex",
        flexDirection:"row",
        justifyContent:"center",
        alignitem:"center",
    }}>
        <div class="mx-3">
    <input type="email" class="form-control" id="minSup" placeholder="Min Sup" />
        </div>
        <div class="mx-3">
    <input type="email" class="form-control" id="minConf" placeholder="Min Conf" />
        </div>
    </div>
    <div className='btn-container'>
    {/* onSubmit={handleSubmit} */}
    <button onClick={loadData}  style={btns} class="btn btn-primary" type="submit">Sample Data</button>
    <button onClick={handleSubmit}  style={btns} class="btn btn-primary" type="submit">Generate</button>
    <button onClick={addRow} style={btns} class="btn btn-primary ml-4" type="submit">Add Row</button>
    <button onClick={removeRow} style={btns} class="btn btn-danger ml-4" type="submit">Delete Row</button>
    <button onClick={clear} style={btns} class="btn btn-danger ml-4" type="submit">Clear</button>
    </div>
    <div id='result' className='container' style={{
        marginTop: '50px',
    }}>
      {/* <h1 style={{
        marginBottom: '25px',
    }}> Rules </h1> */}
    </div>
    </>
  )
}
