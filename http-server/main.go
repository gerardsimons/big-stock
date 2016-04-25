package main

import (
	"fmt"
	"html/template"
	"io/ioutil"
	"net/http"
	"path"
)

type SessionDir struct {
	FilePaths []string
	Name      string
}

// func renderTemplate(w http.ResponseWriter, tmpl string, p *Page) {
// 	t, _ := template.ParseFiles(tmpl + ".html")
// 	t.Execute(w, p)
// }

func handler(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "Hi there, I love %s!", req.URL.Path[1:])
}

// List the session folders
func sessions(w http.ResponseWriter, req *http.Request) {
	// Iterate over all the dirs
	// t := template.New("list") // Create a template.
	fp := path.Join("templates", "list.html")
	tmpl, err := template.ParseFiles(fp) // Parse template file.

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	} else {
		rootDir := "/Users/gerard/bigstock-data"
		files, _ := ioutil.ReadDir(rootDir)
		dirs := make([]SessionDir, 0, 10)

		for _, f := range files {
			dirs = append(dirs, SessionDir{Name: f.Name()})
		}

		// t.Execute(w, dirOne) // merge.
		if err := tmpl.Execute(w, dirs); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
	}

}

func main() {
	// Routes
	http.HandleFunc("/", handler)
	http.HandleFunc("/sessions", sessions)

	// Init
	http.ListenAndServe(":8000", nil)
}
