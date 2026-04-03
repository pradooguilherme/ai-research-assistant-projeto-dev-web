package com.airesearch.backend.model;

import jakarta.persistence.*;

import java.util.List;

@Entity
public class DocumentEmbedding {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long documentId;

    @OneToOne
    @JoinColumn(name = "document_id", referencedColumnName = "id")
    private Document document;

    @Column(columnDefinition = "float8[]")
    private List<Double> embedding;

    public DocumentEmbedding() {
    }

    public DocumentEmbedding(Document document, List<Double> embedding) {
        this.document = document;
        this.embedding = embedding;
    }

    public Long getDocumentId() {
        return documentId;
    }

    public void setDocumentId(Long documentId) {
        this.documentId = documentId;
    }

    public Document getDocument() {
        return document;
    }

    public void setDocument(Document document) {
        this.document = document;
    }

    public List<Double> getEmbedding() {
        return embedding;
    }

    public void setEmbedding(List<Double> embedding) {
        this.embedding = embedding;
    }

    @Override
    public String toString() {
        return "DocumentEmbedding{" +
                "documentId=" + documentId +
                ", document=" + document +
                ", embedding=" + embedding +
                '}';
    }
}
