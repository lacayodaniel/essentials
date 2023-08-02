// create an object named React, has methods to use React library
import React from "react";
import ReactDOM from "react-dom";

// JSX is HTML style blended into JavaScript
// browsers cannot run JSX, first it must be compiled into JS

// an example of a JSX element
// <h1>hello world</h1>
// it looks exactly like HTML

// JSX elements are treated as JS expressions
// they can be saved in a variable, passed to a function, stored in an object or array, etc


// JSX element saved in a variable
const navBar = <nav>I am a nav bar</nav>;

// JSX  elements stored in an object
const myTeam = {
  center: <li>Benzo Walli</li>,
  powerForward: <li>Rasha Loa</li>,
  smallForward: <li>Tayshaun Dasmoto</li>,
  shootingGuard: <li>Colmar Cumberbatch</li>,
  pointGuard: <li>Femi Billon</li>
};

// JSX attr.
my-attribute-name="my-attribute-value";

// JSX elements with attributes
<a href='http://www.google.com'>Welcome to google!</a>;
const title = <h1 id='title'>Introduction to React.js: Part I</h1>;

// JSX element can have mult. attr. just like HTML
const panda = <img src='images/panda.jpg' alt='panda' width='500px' height='500px' />;

// nested JSX elements, note multiline nesting must be encaps. in "()"
const theExample = (
  <a href="https://www.example.com">
    <h1>
      Click me!
    </h1>
  </a>
); // end of multiline nested expression
// the ";" indicates the end of a line, this is why the body above has no ";"


// JSX has a rule that
// The first opening tag and the final closing tag of a JSX expression must belong to the same JSX element!
const blog = (
  <div> removing this div would violate this rule and throw an error
    <img src="pics/192940u73.jpg" />
    <h1>
      Welcome to Dan's Blog!
    </h1>
    <article>
      Wow I had the tastiest sandwich today.  I <strong>literally</strong> almost freaked out.
    </article>
  </div>
);


// rendering the elements
// The first argument is appended to whatever element is selected by the second argument
// note we have to import to get this to work, see first two lines
ReactDOM.render(<h1>Render me!</h1>, document.getElementById("app"));
// note the render method only updates elements that have changed
// DOM = Document Object Model


// running regular JS inside JSX
ReactDOM.render(<h1>{2+3}</h1>, document.getElementById("app")); // 5


// using varibles to set attributes
const pics = {
  panda: "http://bit.ly/1Tqltv5",
  owl: "http://bit.ly/1XGtkM3",
  owlCat: "http://bit.ly/1Upbczi"
};

const pandas = (
  <img
    src={pics.pandas}
    alt="Lazy Panda" />
);

const owl = (
  <img
    src={pics.owl}
    alt="Unimpressed Owl" />
);

const owlCat = (
  <img
    src={pics.owlCat}
    alt="Ghastly Abomination" />
);

// list of events to listen for
// https://reactjs.org/docs/events.html#supported-events
