import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Signup from "./pages/signup";
// import Posts from "./pages/Posts";
//  | <Link to="/posts">Posts</Link>

export default function App() {
  return (
    <BrowserRouter>
      <nav style={{ padding: "10px", background: "#eee" }}>
        <Link to="/">Home</Link> | <Link to="/signup">Signup</Link>
      </nav>

      <Routes>
        <Route path="/" element={<h1>Welcome to Non-Profit Community</h1>} />
        {/* <Route path="/posts" element={<Posts />} /> */}
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}