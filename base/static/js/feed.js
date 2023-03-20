document.addEventListener("DOMContentLoaded", () => {
  tweet_body = document.querySelectorAll(".tweet-body");

  tweet_body.forEach((element) => {
    element.onclick = () => {
      parentElement = element.parentElement;
      id = parentElement.dataset.id;
      location.replace(`http://127.0.0.1:8000/tweet/${id}`);
      history.pushState(
        { id: id },
        "tweeter",
        `http://127.0.0.1:8000/tweet/${id}`
      );
    };
  });
});
