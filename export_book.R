file.remove("_main.Rmd")

### HTML

bookdown::render_book("index.Rmd", output_format = "bookdown::gitbook", clean = TRUE,
            output_dir = "HTML/", 
            encoding = "UTF-8")

### Epub

bookdown::render_book("index.Rmd", output_format = "bookdown::epub_book", clean = TRUE,
                      output_dir = "../Public/PfP_book/Epub/", 
                      encoding = "UTF-8")

### Kindle

bookdown::kindlegen(epub = "../Public/PfP_book/Epub/_main.epub")

### PDF
### as LaTeX is not working, we do a workaround via Word, which needs manual conversion to PDF

bookdown::render_book("index.Rmd", output_format = "bookdown::word_document2", clean = T,
                     output_dir = "../Public/PfP_book/PDF",
                    encoding = "UTF-8")

