package com.airesearch.backend.model;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.util.List;

@Entity
public class Document {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String category;
    private String category_code;
    private LocalDate publication_date;
    private LocalDate updated_date;
    private List<String> authors;
    private String first_author;
    @Column(columnDefinition = "TEXT")
    private String summary;
    private Long summary_word_count;
    @Column(columnDefinition = "TEXT")
    private String text;
    @Column(columnDefinition = "TEXT")
    private String text_no_stopwords;


    public Document() {
    }

    public Document(Long id, String title, String category, String category_code, LocalDate publication_date, LocalDate updated_date, List<String> authors, String first_author, String summary, Long summary_word_count, String text, String text_no_stopwords) {
        this.id = id;
        this.title = title;
        this.category = category;
        this.category_code = category_code;
        this.publication_date = publication_date;
        this.updated_date = updated_date;
        this.authors = authors;
        this.first_author = first_author;
        this.summary = summary;
        this.summary_word_count = summary_word_count;
        this.text = text;
        this.text_no_stopwords = text_no_stopwords;
    }

    public Document(String title, String category, String category_code, LocalDate publication_date, LocalDate updated_date, List<String> authors, String first_author, String summary, Long summary_word_count, String text, String text_no_stopwords) {
        this.title = title;
        this.category = category;
        this.category_code = category_code;
        this.publication_date = publication_date;
        this.updated_date = updated_date;
        this.authors = authors;
        this.first_author = first_author;
        this.summary = summary;
        this.summary_word_count = summary_word_count;
        this.text = text;
        this.text_no_stopwords = text_no_stopwords;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getCategory_code() {
        return category_code;
    }

    public void setCategory_code(String category_code) {
        this.category_code = category_code;
    }

    public LocalDate getPublication_date() {
        return publication_date;
    }

    public void setPublication_date(LocalDate publication_date) {
        this.publication_date = publication_date;
    }

    public LocalDate getUpdated_date() {
        return updated_date;
    }

    public void setUpdated_date(LocalDate updated_date) {
        this.updated_date = updated_date;
    }

    public List<String> getAuthors() {
        return authors;
    }

    public void setAuthors(List<String> authors) {
        this.authors = authors;
    }

    public String getFirst_author() {
        return first_author;
    }

    public void setFirst_author(String first_author) {
        this.first_author = first_author;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public Long getSummary_word_count() {
        return summary_word_count;
    }

    public void setSummary_word_count(Long summary_word_count) {
        this.summary_word_count = summary_word_count;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getText_no_stopwords() {
        return text_no_stopwords;
    }

    public void setText_no_stopwords(String text_no_stopwords) {
        this.text_no_stopwords = text_no_stopwords;
    }

    @Override
    public String toString() {
        return "Document{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", category='" + category + '\'' +
                ", category_code='" + category_code + '\'' +
                ", publication_date=" + publication_date +
                ", updated_date=" + updated_date +
                ", authors=" + authors +
                ", first_author='" + first_author + '\'' +
                ", summary='" + summary + '\'' +
                ", summary_word_count=" + summary_word_count +
                ", text='" + text + '\'' +
                ", text_no_stopwords='" + text_no_stopwords + '\'' +
                '}';
    }
}
