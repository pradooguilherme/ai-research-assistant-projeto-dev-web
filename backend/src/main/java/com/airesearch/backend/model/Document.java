package com.airesearch.backend.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

import java.time.OffsetDateTime;
import java.util.List;

@Entity
public class Document {
    @Id
    @GeneratedValue
    private Long id;
    private String name;
    private String main_category;
    private String summary;
    private List<String> authors;
    private OffsetDateTime publication_date;

    public Document() {
    }

    public Document(Long id, String name, String main_category, String summary, List<String> authors, OffsetDateTime publication_date) {
        this.id = id;
        this.name = name;
        this.main_category = main_category;
        this.summary = summary;
        this.authors = authors;
    }

    public Document(String name, String main_category, String summary, List<String> authors, OffsetDateTime publication_date){
        super();
        this.name = name;
        this.main_category = main_category;
        this.summary = summary;
        this.authors = authors;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getMain_category() {
        return main_category;
    }

    public String getSummary() {
        return summary;
    }

    public List<String> getAuthors() {
        return authors;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setMain_category(String main_category) {
        this.main_category = main_category;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public void setAuthors(List<String> authors) {
        this.authors = authors;
    }

    @Override
    public String toString() {
        return "Document{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", main_category='" + main_category + '\'' +
                ", summary='" + summary + '\'' +
                ", authors=" + authors +
                '}';
    }
}
