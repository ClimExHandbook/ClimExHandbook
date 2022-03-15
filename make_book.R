
# make book
withr::with_dir("webpage/", {
  bookdown::render_book('index.Rmd', 'bookdown::bs4_book',  output_dir = "../docs/")
})
