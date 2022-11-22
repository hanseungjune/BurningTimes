<template>
    <div>
      <div class="row">
          <div id="reviews_title" class="col-3">Review</div>
      </div>
      <div class="row">
        <div
        v-for="(review) in movie.reviews"
        :key="review.id"
        class="reviews">
            {{review.movie.title}} |
            {{review.title}} |
            {{review.user}} |
            {{review.created_at}} |
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
      name: 'DetailReviews',
      props: {
          movie:Object,
      }
  }
  </script>
  
  <style>
    .reviews {
      margin: 0px 5px;
      font-size: 18px;
      text-align: left;
    }

    #reviews_title {
        width: 200px;
        height: 30px;
        text-align: center;
        font-size: 20px;
        margin-left: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
        background-color: green;
        color: white;
        border-radius: 5px;
    }

    #reviews_list {
        text-align: center;
    }

    #actor_link{
        text-decoration: none;
        color: black;
        font-weight: bold;
    }
  </style>