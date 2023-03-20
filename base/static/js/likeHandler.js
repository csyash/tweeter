document.addEventListener("DOMContentLoaded", () => {
  heart_icon = document.querySelectorAll(".heart-icon");
  RT_icon = document.querySelectorAll(".retweet-icon");

  heart_icon.className = "heart-icon-liked";
  RT_icon.forEach((icon) => {
    icon.onclick = () => {
      clickHandler(icon, "retweet");
    };
  });
  heart_icon.forEach((icon) => {
    /*
      icon.onclick = () => {
      parentElement = icon.parentElement.parentElement.parentElement;
      tweet_id = parentElement.dataset.id;

      icon_parent = icon.parentElement;
      tweet_likes_span = icon_parent.querySelector("span");
      tweet_likes = parseInt(tweet_likes_span.innerHTML);
      tweet_likes_span.innerHTML = tweet_likes + 1;

      fetch(`http://127.0.0.1:8000/tweet/${tweet_id}/like`, {
        method: "POST",
      });
    
     };
    */

    icon.onclick = () => {
      icon.className += " heart-icon-liked";
      clickHandler(icon, "like");
    };
  });
});

function clickHandler(icon, action) {
  parentElement = icon.parentElement.parentElement.parentElement;
  tweet_id = parentElement.dataset.id;
  console.log("fired");
  icon_parent = icon.parentElement;
  tweet_likes_span = icon_parent.querySelector("span");
  tweet_likes = parseInt(tweet_likes_span.innerHTML);
  tweet_likes_span.innerHTML = tweet_likes + 1;

  fetch(`http://127.0.0.1:8000/tweet/${tweet_id}/${action}`, {
    method: "POST",
  });
}
