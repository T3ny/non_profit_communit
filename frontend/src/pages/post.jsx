import { useEffect, useState } from "react";
import axios from "axios";

export default function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/benfit_community/posts/") // Your Django posts endpoint
      .then((res) => {
        setPosts(res.data);
      })
      .catch((err) => {
        console.error("Error fetching posts:", err);
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Community Posts</h1>
      {posts.length > 0 ? (
        posts.map((post) => (
          <div key={post.id} style={{ marginBottom: "10px", border: "1px solid #ddd", padding: "10px" }}>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
          </div>
        ))
      ) : (
        <p>No posts yet.</p>
      )}
    </div>
  );
}
