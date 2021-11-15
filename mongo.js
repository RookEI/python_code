b.books.insertMany([
  {
    "name": "Confident Ruby",
    "publishedDate": new Date(),
    "authors": [
      { "name": "Avdi Grimm" }
    ]
  },
  {
    "name": "The War of Art",
    "publishedDate": new Date(),
    "authors": [
      {"name": "Steven Pressfield"}
    ]
  },
  {
    "name": "Blink",
    "publishedDate": new Date(),
    "authors": [
      {"name": "Malcolm Gladwell"}
    ]
  }
])





db.books.insert( 
  {
    "name": "Deep Work: Rules for Focused Success in a Distracted World",
    "publishedDate": new Date(),
    "reviews": 100,
    "authors": [
      {"name": "Cal Newport"}
    ]
  }
)
