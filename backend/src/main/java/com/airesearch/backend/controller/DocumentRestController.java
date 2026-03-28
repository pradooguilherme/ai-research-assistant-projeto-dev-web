package com.airesearch.backend.controller;

import com.airesearch.backend.model.Document;
import com.airesearch.backend.service.DocumentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("document")
public class DocumentRestController {

    private final DocumentService documentService;

    public DocumentRestController(DocumentService documentService) {
        this.documentService = documentService;
    }

    @GetMapping
    public ResponseEntity<Iterable<Document>> getFirst100Documents() {
        return ResponseEntity.ok(documentService.findFirst100Documents());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Document> getDocumentById(@PathVariable Long id){
        return ResponseEntity.ok(documentService.findById(id));
    }

    @PostMapping
    public ResponseEntity<Document> insertDocument(@RequestBody Document document){
        documentService.insert(document);
        return ResponseEntity.ok(document);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Document> deleteDocument(@PathVariable Long id){
        documentService.delete(id);
        return ResponseEntity.ok().build();
    }
}
