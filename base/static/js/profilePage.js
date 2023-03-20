document.addEventListener("DOMContentLoaded", () => {
  follow_btn = document.querySelector(".follow-btn");
  unfollow_btn = document.querySelector(".unfollow-btn");

  url = window.location.href;
  console.log(follow_btn, unfollow_btn);

  follow_btn.onclick = () => {
    fetch(`${url}/follow`, {
      method: "POST",
    });
  };

  unfollow_btn.onclick = () => {
    fetch(`${url}/unfollow`),
      {
        method: "POST",
      };
  };
});
