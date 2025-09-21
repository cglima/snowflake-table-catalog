import { Table } from '../domain/entities';
import { TableRepository } from '../application/ports';

export class ApiTableRepository implements TableRepository {
  async getTables(): Promise<Table[]> {
    const response = await fetch('http://127.0.0.1:8000/tables');
    if (!response.ok) {
      throw new Error('Failed to fetch tables');
    }
    const data = await response.json();
    return data;
  }
}
