import React from 'react';
import ReactDOM from 'react-dom';
import {Store,Index,Page}  from './components/app.jsx';
import {BrowserRouter, Link, Route, Router, Switch} from 'react-router-dom';
import styled from 'styled-components'
//import {Store} from '/components/app.jsx';

require("!style-loader!css-loader!./css/style.css");
require("!style-loader!css-loader!./css/highlight.js/8.4.0/styles/monokai-sublime.css");

var STORE = new Store();
var AppContext = {"store":STORE};
/**
 Store.import( indexer, url, onSuccess )
 store.register to an index and that's it
 store.register ( "page", (newValue)  => {
    console.log(newValue);
 });
 * 
 */
AppContext.store.update(function(store,data){
  data.map( 
    (entry) => {
        var k = "page-" + entry["file"];
        store[k] = entry;
        console.log("k:",k);
    }
  );
}, "/content/index.json"   ,  (responseData) => {
    
  console.log("data-loaded:",Object.keys(AppContext.store.data));
  console.log("data-loaded-example:",Object.keys(AppContext.store.get("page-python_getset")));
  
  
});



class Eraror extends React.Component {
  render() { return (<div>Error: {this.props} </div> );}
}

const Header=styled.div`


`
const Content=styled.div`
`
const Footer=styled.div`
  
  
`

const Layout = styled.div`
  display: grid; 
  grid-template-columns: 1fr;
  grid-auto-columns: minmax(100px,auto);
  grid-column-gap:  1em;
  grid-row-gap: 1em;
  padding: 0 20px;

  & > div {
    //background: #eee;
    padding: 1em;

  }

  & > div:nth-child(odd){
    //background: #ddd;
  }

  
  
`

class App extends React.Component {
  render(){
    return (

      <Layout> 
  
        <Header>  
          <Link to="/">Go Home Again:  </Link>
        </Header>


        <Content>  
          <Switch>
              <Route exact path='/' render={ 
                  (props) => { return (<Index  params={props.params} context={AppContext}/> )} 
                  
              } />

              <Route path='/page/:name' render={ 
                  (props) => { return (<Page  match={props.match} context={AppContext}/> )} 
                  
              }/>
              <Route component={Error} />
          </Switch>


        </Content> 

        <Footer>
          Footer 
        </Footer>
      

        
      </Layout> 
    );
  }

}

/*
<Switch>
          <Route exact  path='/' component={Index} />
        </Switch> 

 */

ReactDOM.render( ( 
  <BrowserRouter>           
      <App/> 
    </BrowserRouter> 
     )  ,
    document.getElementById('root')
)


